import React, { useState } from 'react';
import fetchData from '../Fetch';
import Table from '../components/StudentDetails/Table';

export default function Updates() {
	
	return (
		<div className='w-full'>
			<h1 className='font-extrabold text-4xl text-center my-3 w-full '>
				List of student and their details
			</h1>
			<Table />
		</div>
	);
}
