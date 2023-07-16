import React, { useState } from 'react';
import fetchData from '../Fetch';
import Table from '../components/StudentDetails/Table';

export default function Updates() {
	const { data, isLoading, error, count } = fetchData(
		'http://127.0.0.1:8000/api/students/111/get/',
	);
	console.log(data);

	return (
		<div>
			<h1 className='font-extrabold text-4xl my-3'>
				List of student and their details
			</h1>
			<Table />
		</div>
	);
}
