import fetchData from '../../Fetch';

export default function Table() {
	const { data, isLoading, error } = fetchData(
		'http://127.0.0.1:8000/api/students/',
	);

	return (
		<>
			<div className='mt-5 flex justify-center'>
				<div className='overflow-x-auto h-80'>
					<table className='table table-xs table-pin-rows '>
						<thead>
							<tr>
								<th></th>
								<th>Name</th>
								<th>Program</th>

								<th>Index</th>
								<th>Level</th>
								<th>Email</th>
								<th>Year Enrolled</th>
							</tr>
						</thead>
						<tbody
							
							className={`border border-x--white capitalize
								${isLoading
									? `loading loading-ring loading-md`
									: ''}`
							}>
							{data &&
								data.map((student, index) => (
									<tr key={index}>
										<th>{index + 1}</th>
										<td>{student.name}</td>
										<td>
											{student.program.name}
										</td>

										<td>{student.index}</td>
										<td>{student.level}</td>
										<td>{student.email}</td>
										<td>
											{student.year_enrolled}
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
