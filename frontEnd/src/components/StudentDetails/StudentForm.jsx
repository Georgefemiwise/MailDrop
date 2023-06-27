import React, { useEffect, useState } from 'react';
// import Navbar from './components/NavBar';
// import Stats from './components/Stats';
// import Fetch from './Fetch';
// import React from 'react';

export default function StudentForm() {
	const [newStudent, setNewStudent] = useState({
		program: '',
		level: '',
		year_enrolled: '',
		total_number_in_class: '',
		email: '',
	});

	const handleInputChange = (event) => {
		const { name, value } = event.target;
		setNewStudent((prevStudent) => ({
			...prevStudent,
			[name]: value,
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
					total_number_in_class: '',
					email: '',
				});
			} else {
				console.log('Error sending data to the backend');
			}
		} catch (error) {
			console.log('Error sending data to the backend:', error);
		}
	};

	return (
		<div className='card w-96 bg-neutral text-neutral-content'>
			<div className='card-body items-center text-center'>
				<h2 className='card-title font-black'>Student Form!</h2>
				<p className='text-xs'>
					Create an entire class of student{' '}
				</p>{' '}
				<form
					onSubmit={handleSubmit}
					className='flex flex-col gap-2 w-full '>
					<input
						type='text'
						name='program'
						value={newStudent.program}
						onChange={handleInputChange}
						placeholder='Program'
						className='input input-bordered w-full max-w-xs '
					/>
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
						value={newStudent.total_number_in_class}
						onChange={handleInputChange}
						placeholder='Class total'
						className='input input-bordered w-full max-w-xs '
					/>
					{/* <input
						type='text'
						name='year'
						value={newStudent.year}
						onChange={handleInputChange}
						placeholder='Year'
						className='input input-bordered w-full max-w-xs '
					/> */}
					{/* <input
						type='text'
						name='index'
						value={newStudent.index}
						onChange={handleInputChange}
						placeholder='Index'
						className='input input-bordered w-full max-w-xs '
					/> */}
					{/* <input
						type='email'
						name='email'
						value={newStudent.email}
						onChange={handleInputChange}
						placeholder='Email'
						className='input input-bordered w-full max-w-xs '
					/> */}

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
