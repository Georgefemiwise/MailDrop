import React from 'react';

import NavBar from '../components/Navigation/NavBar';
export default function SideBarFrame() {
	return (
		<aside className='bg-neutral-content min-w-[10rem] '>
			<div className='w- min-w-fit flex-shrink flex-grow-0  flex justify-between'>
				<div className='sticky top-0  w-full h-full'>
					<NavBar />
				</div>
			</div>
		</aside>
	);
}
