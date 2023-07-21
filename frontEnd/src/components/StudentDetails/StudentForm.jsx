import React, { useEffect, useState } from 'react';
import fetchData from '../../Fetch';

export default function StudentForm() {
	const { data, isLoading, error } = fetchData(
		'http://127.0.0.1:8000/api/programs/',
	);
	
	const [newStudent, setNewStudent] = useState({
		program: { abbreviation: '', name: '' },
		level: '',
		year_enrolled: '',
		classTotal: '',
	});

	const handleInputChange = (event) => {
		const { name, value } = event.target;
		setNewStudent((prevStudent) => ({
			...prevStudent,
			[name]: value,
		}));
	};

	const handleProgramChange = (event) => {
		const { value, text } = event.target.selectedOptions[0];
		setNewStudent((prevStudent) => ({
			...prevStudent,
			program: { abbreviation: value, name: text },
		}));
	};


	const handleSubmit = async (event) => {
		event.preventDefault();

		try {
			const response = await fetch(
				'http://127.0.0.1:8000/api/students/create/',
				{
					method: 'POST',
					headers: {
						'Content-Type': 'application/json',
					},
					body: JSON.stringify(newStudent),
				},
			);

			if (response.ok) {
				// Data sent successfully, update the student list
				const createdStudent = await response.json();
				console.log('Created student:', createdStudent);
				setNewStudent({
					program: '',
					level: '',
					year_enrolled: '',
					classTotal: '',
				});
			} else {
				console.log(
					'Error sending data to the backend for some reason',
				);
			}
		} catch (error) {
			console.log('Fetch Error sending data to the backend:', error);
		}
	};

	const dateEnrolled = new Date();
	const dateEnrolledList = [
		dateEnrolled.getFullYear(),
		dateEnrolled.getFullYear() - 1,
		dateEnrolled.getFullYear() - 2,
		dateEnrolled.getFullYear() - 3,
	];
	return (
		<div className='card w-full bg-neutral text-neutral-content max-h-[30rem]'>
			<div className='card-body items-center text-center '>
				<h2 className='card-title font-black text-5xl'>Student Form!</h2>
				<p className='text-lg'>Create an entire class of student</p>

				<form
					method='post'
					onSubmit={handleSubmit}
					className='flex flex-col gap-2 min-w-[30rem] '>
					<input
						type='text'
						name='level'
						value={newStudent.level}
						onChange={handleInputChange}
						placeholder='Level'
						className='input input-bordered w-full max-w-lg '
					/>
					<input
						type='text'
						name='year_enrolled'
						value={newStudent.year_enrolled}
						onChange={handleInputChange}
						placeholder='year enrolled'
						className='input input-bordered w-full max-w-lg '
					/>
					{/* {dateEnrolledList.map((date) => { return date + ' ' + dateEnrolled })} */}

					{/* <div className='form-control flex flex-row items-center align-middle'>
						{dateEnrolledList.map((date, index) => (
							<label
								className={`cursor-pointer flex border border-gray-600 p-2 ${
									date == dateEnrolledList[0]
										? 'ml-0'
										: 'ml-5'
								}`}>
								<input
									type='radio'
									name='year_enrolled'
									className='radio checked:bg-red-500'
									value={newStudent.year_enrolled}
									onChange={handleInputChange}
								/>
								<span className='ml-2'>{date}</span>
							</label>
						))}
					</div> */}

					<input
						type='number'
						name='classTotal'
						value={newStudent.classTotal}
						onChange={handleInputChange}
						placeholder='Class total'
						className='input input-bordered w-full max-w-lg'
					/>

					<select
						name='program'
						value={newStudent.program.abbreviation}
						onChange={handleProgramChange}
						className='select select-bordered w-full max-w-lg'>
						<option
							disabled
							value=''
							selected
							className='bg-slate-200'>
							choose a program
						</option>
						{data &&
							!isLoading &&
							data.map((item, index) => (
								<option
									key={index}
									value={item.abbreviation}>
									{item.name}
								</option>
							))}
					</select>

					<div className='card-actions '>
						<button type='submit' className='btn btn-primary'>
							create student
						</button>
					</div>
				</form>
			</div>
		</div>
	);
}
