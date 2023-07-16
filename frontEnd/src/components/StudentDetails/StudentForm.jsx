import React, { useEffect, useState } from 'react';
import fetchData from '../../Fetch';

export default function StudentForm() {
	const { data, isLoading, error } = fetchData(
		'http://127.0.0.1:8000/api/programs/',
	);

	const [newStudent, setNewStudent] = useState({
		program: { id: '', name: '' }, // Initialize program as a nested dictionary
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
			program: { id: value, name: text },
		}));
	};

	console.log(newStudent);

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

	return (
		<div className='card w-96 bg-neutral text-neutral-content max-h-[30rem]'>
			<div className='card-body items-center text-center '>
				<h2 className='card-title font-black'>Student Form!</h2>
				<p className='text-xs'>Create an entire class of student</p>

				<form
					method='post'
					onSubmit={handleSubmit}
					className='flex flex-col gap-2 w-full '>
					<input
						type='text'
						name='level'
						value={newStudent.level}
						onChange={handleInputChange}
						placeholder='Level'
						className='input input-bordered w-full max-w-xs '
					/>
					<input
						type='text'
						name='year_enrolled'
						value={newStudent.year_enrolled}
						onChange={handleInputChange}
						placeholder='year enrolled'
						className='input input-bordered w-full max-w-xs '
					/>
					<input
						type='text'
						name='classTotal'
						value={newStudent.classTotal}
						onChange={handleInputChange}
						placeholder='Class total'
						className='input input-bordered w-full max-w-xs'
					/>

					<select
						name='program'
						value={newStudent.program.id.toString()} // Convert id to a string
						onChange={handleProgramChange}
						className='select select-bordered w-full max-w-xs'>
						<option disabled value=''>
							choose a program
						</option>
						{data &&
							!isLoading &&
							data.map((item) => (
								<option key={item.id} value={item.id}>
									{item.name}
								</option>
							))}
					</select>

					<div className='card-actions '>
						<button type='submit' className='btn btn-primary'>
							create
						</button>
					</div>
				</form>
			</div>
		</div>
	);
}
