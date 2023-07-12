import fetchData from '../../Fetch';
import { Link } from 'react-router-dom';

export default function Table() {
	const { data, isLoading, error } = fetchData(
		'http://127.0.0.1:8000/api/students/',
	);

	return (
		<>
			<div className='mt-5 flex justify-center'>
				<div className='overflow-x-auto h-96'>
					<table className='table table-pin-rows  w-10/12'>
						<thead>
							<tr>
								<th>sn</th>
								<th>Program</th>
								<th>Index</th>
								<th>Email</th>
								<th>btn</th>
							</tr>
						</thead>
						<tbody
							className={`capitalize justify-center
								${isLoading ? `loading loading-ring loading-lg` : ''}`}>
							{data &&
								data.map((student, index) => (
									<tr key={index}>
										<td className='text-slate-500 text-opacity-50'>
											{index + 1}
										</td>

										<td>
											{student.program.name}
										</td>

										<td>{student.index}</td>

										<td>{student.email}</td>

										<th>
											{/* The button to open modal */}
											<label
												htmlFor={
													student.email
												}
												className='btn btn-xs'>
												details
											</label>

											{/* Put this part before </body> tag */}
											<input
												type='checkbox'
												id={student.email}
												className='modal-toggle'
											/>
											<div className='modal'>
												<div className='modal-box p-10'>
													<h3 className='font-bold text-lg'>
														Student
														Details
													</h3>
													<p className='pt-10'>
														<span className='mr-10 badge-lg badge badge-outline'>
															ID:
														</span>
														{
															student.id
														}
													</p>
													<p className='pt-5 w-full font-extrabold'>
														<span className='mr-10 badge-lg badge badge-outline'>
															Index:
														</span>
														{
															student.index
														}
													</p>
													<p className='pt-5 w-full font-extrabold'>
														<span className='mr-10 badge-lg badge badge-outline'>
															Email:
														</span>
														{
															student.email
														}
													</p>

													<p className='pt-5 w-full font-extrabold'>
														<span className='mr-10 badge-lg badge badge-outline'>
															Program:
														</span>
														{
															student
																.program
																.name
														}
													</p>
													<p className='pt-5 w-full font-extrabold'>
														<span className='mr-10 badge-lg badge badge-outline'>
															Level:{' '}
														</span>
														{
															student.level
														}
													</p>
													<p className='pt-5 w-full font-extrabold'>
														<span className='mr-10 badge-lg badge badge-outline'>
															Year
														</span>
														Enrolled:
														{
															student.year_enrolled
														}
													</p>

													<div className='modal-action'>
														<label
															htmlFor={
																student.email
															}
															className='btn'>
															Close!
														</label>
													</div>
												</div>
											</div>
										</th>
									</tr>
								))}
						</tbody>
					</table>
				</div>
			</div>
		</>
	);
}
