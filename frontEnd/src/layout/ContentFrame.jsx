import React from 'react';
import { Outlet } from 'react-router-dom';

export default function ContentFrame() {
	return (
		<div className={`content flex flex-1 p-5   `}>
			<Outlet />
		</div>
	);
}
