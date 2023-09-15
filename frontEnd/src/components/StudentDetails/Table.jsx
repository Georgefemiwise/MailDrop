import fetchData from '../../Fetch';
import { Link } from 'react-router-dom';

export default function Table() {
	const { data, isLoading, error } = fetchData(
		'http://127.0.0.1:8000/api/students/',
	);

	return (
		<>
			<div className='mt-5 flex justify-center w-full'>
				<div className='overflow-x-auto h-96'>
					<table className='table-sm min-w-[80rem] text-center'>
						<thead className='font-extrabold text-3xl'>
							<tr>
								<th>S/N</th>
								<th>Program</th>
								<th>Index</th>
								<th>Email</th>
								<th></th>
							</tr>
						</thead>
						<tbody
							className={`capitalize 
								${isLoading ? `loading loading-ring loading-lg` : ''}`}>
							<tr>
								<td></td>
								<td></td>
							</tr>
							{data &&
								data.map((student, index) => (
									<tr
										key={index}
										className='bg-inherit hover:bg-gray-700'>
										<td className='text-slate-500 text-opacity-50'>
											{index + 1}
										</td>

										<td>
											{
												student.program
													.programName
											}
										</td>

										<td>
											{student.student.index}
										</td>

										<td className='lowercase'>
											{student.student.email}
										</td>
									</tr>
								))}
						</tbody>
					</table>
				</div>
			</div>
		</>
	);
}
