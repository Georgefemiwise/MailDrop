import React from 'react';
import StudentForm from '../components/StudentDetails/StudentForm';
import fetchData from '../Fetch';

export default function CreateStudent() {
	const { data, isLoading, error } = fetchData(
		'http://127.0.0.1:8000/api/programs/',
	);
	console.log(data);

	const dateEnrolled = new Date();
	const dateEnrolledList = [
		dateEnrolled.getFullYear(),
		dateEnrolled.getFullYear() - 1,
		dateEnrolled.getFullYear() - 2,
		dateEnrolled.getFullYear() - 3,
	];

	return (
		<div className='flex gap-5'>
			{/* <div className='card  w-[40rem] h-[40rem] overflow  bg-base-100 shadow-xl'>
				<div className='card-body'>
					<h3 className='card-title mb-5 font-black text-2xl'>
						Send a Message
					</h3>

					<div className='student-selector '>
						<h4 className='py-2 capitalize'>
							select program
						</h4>
						<div className='student-selector flex border p-1 rounded border-success'>
							{data &&
								!isLoading &&
								data.map((item) => (
									<div className='form-control'>
										<label className='label cursor-pointer'>
											<input
												type='radio'
												name='program'
												className='radio checked:bg-red-500'
												value={data.name}
											/>
											<span className='label-text ml-2'>
												{item.name}
											</span>
										</label>
									</div>
								))}
						</div>
					</div>
					<div className='student-selector mb-5'>
						<h4 className='py-2 capitalize'>select year</h4>
						<div className='student-selector flex border p-1 rounded border-success'>
							{dateEnrolledList &&
								dateEnrolledList.map((item, index) => (
									<div className='form-control'>
										<label className='label cursor-pointer'>
											<input
												type='radio'
												name='year'
												className='radio checked:bg-red-500'
												value={item}
											/>
											<span className='label-text ml-2'>
												{item}
											</span>
										</label>
									</div>
								))}
						</div>
					</div>
					<div className='form-control'></div>
					<div className='form-control flex flex-1'>
						<textarea
							placeholder='your Message'
							className='textarea textarea-success textarea-lg w-full h-full'></textarea>
						<p className='text-xs text-gray-400'>
							This input accept text, however if you want
							to insert your link, pls encapsolate it in a
							bracket eg
							[https//www.examplelink.com/nothing]
						</p>
					</div>

					<div className='card-actions justify-end'>
						<button className='btn btn-primary'>
							preview
						</button>
					</div>
				</div>
			</div> */}

			<StudentForm />
		</div>
	);
}
