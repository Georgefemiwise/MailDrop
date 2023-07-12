import React from 'react';
import StudentForm from '../components/StudentDetails/StudentForm';
import fetchData from '../Fetch';

export default function CreateStudent() {
	const { data, isLoading, error } = fetchData(
		'http://127.0.0.1:8000/api/program/all/',
  );
  console.log(data)
	return (
		<div className='flex gap-5'>
			<div className='card  w-[40rem] h-[40rem] overflow  bg-base-100 shadow-xl'>
				<div className='card-body'>
					<h3 className='card-title mb-5 font-black text-2xl'>
						Send a Messages
					</h3>

					<div className='student-selector '>
						<h4 className='py-2 capitalize'>
							select program
						</h4>
						<div className='student-selector flex border p-1 rounded border-success'>
							<div className='form-control'>
								{data &&
									!isLoading &&
									data.map((item) => (
										<label className='label cursor-pointer'>
											<input
												type='radio'
												name='radio-10'
												className='radio checked:bg-red-500'
												
											/>
											<span className='label-text ml-2'>
												{data.name}
											</span>
										</label>
									))}
								{/* <label className='label cursor-pointer'>
									<input
										type='radio'
										name='radio-10'
										className='radio checked:bg-red-500'
										checked
									/>
									<span className='label-text ml-2'>
										Red pill
									</span>
								</label> */}
							</div>
							<div className='form-control'>
								<label className='label cursor-pointer'>
									<input
										type='radio'
										name='radio-10'
										className='radio checked:bg-red-500'
									/>
									<span className='label-text ml-2'>
										Red pill
									</span>
								</label>
							</div>
							<div className='form-control'>
								<label className='label cursor-pointer'>
									<input
										type='radio'
										name='radio-10'
										className='radio checked:bg-red-500'
									/>
									<span className='label-text ml-2'>
										Red pill
									</span>
								</label>
							</div>
							<div className='form-control'>
								<label className='label cursor-pointer'>
									<input
										type='radio'
										name='radio-10'
										className='radio checked:bg-red-500'
									/>
									<span className='label-text ml-2'>
										Red pill
									</span>
								</label>
							</div>
						</div>
					</div>

					<div className='student-selector '>
						<h4 className='py-2 capitalize'>select Year</h4>
						<div className='student-selector flex border p-1 rounded border-success'>
							<div className='form-control'>
								<label className='label cursor-pointer'>
									<input
										type='radio'
										name='radio-11'
										className='radio checked:bg-red-500'
										checked
									/>
									<span className='label-text ml-2'>
										Red pill
									</span>
								</label>
							</div>
							<div className='form-control'>
								<label className='label cursor-pointer'>
									<input
										type='radio'
										name='radio-11'
										className='radio checked:bg-red-500'
										checked
									/>
									<span className='label-text ml-2'>
										Red pill
									</span>
								</label>
							</div>
							<div className='form-control'>
								<label className='label cursor-pointer'>
									<input
										type='radio'
										name='radio-11'
										className='radio checked:bg-red-500'
										checked
									/>
									<span className='label-text ml-2'>
										Red pill
									</span>
								</label>
							</div>
							<div className='form-control'>
								<label className='label cursor-pointer'>
									<input
										type='radio'
										name='radio-11'
										className='radio checked:bg-red-500'
										checked
									/>
									<span className='label-text ml-2'>
										Red pill
									</span>
								</label>
							</div>
						</div>
					</div>

					<textarea
						placeholder='Bio'
						className='textarea textarea-success textarea-lg w-full h-full'></textarea>

					<div className='card-actions justify-end'>
						<button className='btn btn-primary'>
							Buy Now
						</button>
					</div>
				</div>
			</div>

			{/* <StudentForm /> */}
		</div>
	);
}
