import React from 'react';
import Stats from '../components/Stats';
import fetchData from '../Fetch';
import Table from '../components/StudentDetails/Table';

export default function Statistics() {
	const student = fetchData('http://127.0.0.1:8000/api/students/');
	const department = fetchData('http://127.0.0.1:8000/api/departments/');
	const program = fetchData('http://127.0.0.1:8000/api/programs/');

	return (
		<div className='flex flex-col'>
			<div className='stats p-2 gap-1 shadow shadow-white'>
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
			<div className='flex '>
				<div className=''>
					<Stats
						title={'BTECH Student'}
						value={'0'}
						desc={null}
					/>
				</div>
				<Stats title={'HND Student'} value={'0'} desc={null} />
				<Stats title={'Diploma Student'} value={'0'} desc={null} />
				{/* <Table /> */}
			</div>
		</div>
	);
}
