import React from 'react';
import Dashboard from '../../layout/MainFrame';
import fetchData from '../../Fetch';

export default function Stats({ value, title, desc, icon, className }) {
	return (
		<>
			<div className={`stat  border rounded-md ${className}`}>
				<div className='stat-figure text-secondary font-extrabold '>
					{icon}
				</div>
				<div className='stat-title font-extrabold text-lg'>
					{title}
				</div>
				<div className='stat-value text-primary text-5xl'>
					{value >= 1000 ? value + 'K' : value}
				</div>
				<div className='stat-desc mt-2'>{desc}</div>
			</div>
		</>
	);
}
