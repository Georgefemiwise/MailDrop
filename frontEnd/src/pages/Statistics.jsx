import React from 'react';
import Stats from '../components/Stats/Stats';
import fetchData from '../Fetch';
import Table from '../components/StudentDetails/Table';

export default function Statistics() {
	const student = fetchData('http://127.0.0.1:8000/api/students/');
	const department = fetchData('http://127.0.0.1:8000/api/departments/');
	const program = fetchData('http://127.0.0.1:8000/api/programs/');
	function getStudentInprogram(programId) {
		return fetchData(`http://127.0.0.1:8000/api/students/${programId}/`);
	}

	return (
		<div className='container p-3'>
			<h1 className="h1 text-4xl my-4 font-black  text-center">Student Statistics</h1>
			<div className='flex pt-2 gap-1 '>
				<Stats
					title={'Total Student'}
					value={student.count}
					desc={'The total number of student '}
				/>
				<Stats
					value={department.count}
					title={'Total Department'}
					desc={'The total number of departments'}
				/>
				<Stats
					value={program.count}
					title={'Total Programs'}
					desc={'The total number of Programs'}
				/>
			</div>
			<div className='flex  pt-2 gap-1'>
				<Stats
					title={'Bachelor of technology Student'}
					value={getStudentInprogram(1).count}
					desc={null}
				/>

				<Stats
					title={'Higher National Diploma Student'}
					value={getStudentInprogram(2).count}
					desc={null}
				/>
				<Stats title={'Diploma Student'} value={'0'} desc={null} />
			</div>
		</div>
	);
}

{
	/* <Table /> */
}
