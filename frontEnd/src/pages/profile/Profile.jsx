import React, { useState } from 'react';
import { Link } from 'react-router-dom';

export default function Profile() {
	const [editProfile, setEditProfile] = useState({
		companyProfileEdit: false,
		personalProfileEdit: false,
	});

	function personalEditMode() {
		setEditProfile((prev) => !prev.personalProfileEdit);
	}
	function companyEditMode() {
		setEditProfile((prev) => !editProfile.companyProfileEdit);
	}

	const personalProfileInput = [
		{ name: 'username', value: 'Johndoe', type: 'text' },
		{ name: 'first name', value: 'John', type: 'text' },
		{ name: 'last name', value: 'doe', type: 'text' },
		{ name: 'email', value: 'Johndoe@gmail.com', type: 'email' },
		{ name: 'phone', value: '1234567890', type: 'text' },
		{ name: 'DOB', value: '', type: 'date' },
	];

	const companyProfileInput = [
		{ name: 'company name', value: 'Johndoe', type: 'text' },
		{ name: 'company email', value: 'Johndoe@gmail.com', type: 'email' },
	];
	return (
		<div className='p-5'>
			{/* <Link to='edit' className='btn btn-active'>
				edit
			</Link> */}
			<div className='flex gap-5'>
				<div className='card w-3/6 bg-neutral-focus p-8'>
					<form className='flex flex-col'>
						<div className=' text-4xl font-black card-title my-5 flex justify-center '>
							<h2 className='capitalize'>
								personal information
							</h2>
						</div>
						<div className='card-body '>
							{personalProfileInput.map((profile) => (
								<div className='form_control flex gap-5 items-center justify-between'>
									<label
										className='capitalize font-bold text-sm'
										htmlFor={profile.name}>
										{profile.name}
									</label>
									<input
										type={profile.type}
										placeholder='name'
										// value={profile.value}
										disabled={
											!editProfile.personalProfileEdit
										}
										className='input input-primary input-md w-full max-w-md '
									/>
								</div>
							))}
						</div>
						<div className='card-action'>
							<button
								onClick={personalEditMode}
								className='btn btn-primary capitalize'
								type={editProfile.personalProfileEdit && 'submit'}>
								{editProfile.personalProfileEdit
									? 'Save Profile'
									: 'Edit Profile'}
							</button>
						</div>
					</form>
				</div>
			
				<div className='card w-3/6 bg-neutral-focus p-8 h-fit'>
					<form className='flex flex-col'>
						<div className=' text-5xl font-black card-title my-5 flex justify-center '>
							<h2 className='capitalize'>
								personal information
							</h2>
						</div>
						<div className='card-body '>
							{companyProfileInput.map((profile) => (
								<div className='form_control flex gap-5 items-center justify-between'>
									<label
										className='capitalize font-bold text-sm'
										htmlFor={profile.name}>
										{profile.name}
									</label>
									<input
										type={profile.type}
										name={
											'company' + profile.name
										}
										placeholder='name'
										value={profile.value}
										disabled={!editProfile}
										className='input input-primary input-md w-full max-w-md input-disabled'
									/>
								</div>
							))}
						</div>
						<div className='card-action bottom-0'>
							<button
								className='btn btn-primary btn-md capitalize'
								type='submit'>
								{editProfile
									? 'Save Profile'
									: 'Edit Profile'}
							</button>
						</div>
					</form>
				</div>
			</div>
		</div>
	);
}
