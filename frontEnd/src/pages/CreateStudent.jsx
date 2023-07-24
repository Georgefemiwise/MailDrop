import React, { useState } from 'react';
import StudentForm from '../components/StudentDetails/StudentForm';
import fetchData from '../Fetch';
import Form from '../components/Form';

export default function CreateStudent() {
	const [editNow, setEditNow] = useState(false);
	const [inputs, setInputs] = useState({ sname: '', fname:'' });

	const handleInputChange = (event) => {
		const { name, value } = event.target;
		setInputs((prev) => ({
			// ...prev,
			[name]: value,
		}));
		console.log(name, value);
	};

	const startEdite = () => { 
		setEditNow(prev => !prev);
	}
	const handleSubmit =  (event) => {
		event.preventDefault();
	}

	return (
		<div className='flex gap-5'>
			{/* <div className='card  w-[40rem] h-[40rem] overflow  bg-base-100 shadow-xl'>
				<div className='card-body'>
					<form onSubmit={handleSubmit}>
						<input
							type='text'
							placeholder='Level'
							value={inputs.sname}
							onChange={handleInputChange}
							name='sname'
							className={`input input-bordered w-full ${
								editNow &&
								'input-disabled cursor-default '
							}`}
							disabled={editNow}
						/>
						<button
							type='submit'
							onClick={startEdite}
							className='btn btn-primary btn-xs capitalize'>
							{editNow ? 'edit profile' : 'save profile'}
						</button>
					</form>

					<Form />
				</div>
			</div> */}

			<StudentForm />
		</div>
	);
}



