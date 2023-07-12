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
			<h1 className='font-extrabold text-6xl my-3'>
				Get student Detail
			</h1>

			<Table />
		</div>
	);
}
