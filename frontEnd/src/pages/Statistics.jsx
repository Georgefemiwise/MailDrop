import React from 'react';
import Stats from '../components/Stats';
import fetchData from '../Fetch';
import Table from '../components/StudentDetails/Table';

export default function Statistics() {
	const { data, isLoading, error, count } = fetchData(
		'http://127.0.0.1:8000/api/students/',
	);
	return (
		<div className='flex flex-col'>
			<div className=' stats gap-1 shadow shadow-white'>
				<Stats
					value={count}
					title={'Student'}
					icon={'online'}
					desc={'The total number of studenton the database'}
				/>
				<Stats
					value={count}
					title={'Student'}
					desc={'The total number of studenton the database'}
				/>
			</div>
			<div className='table'>
				<Table />
			</div>
		</div>
	);
}
