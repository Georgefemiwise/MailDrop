import React from 'react';

import { Outlet } from 'react-router-dom';
import SideBarFrame from './SideBarFrame';
import NavBar from '../components/Navigation/NavBar';

export default function MainFrame() {
	return (
		<>
			<div className='flex flex-col sm:flex-ro flex-wrap sm:flex-nowrap flex-grow h-screen text-sm'>
				<NavBar />
				{/* <SideBarFrame /> */}
				<main role='main' className='w-full flex-grow pt-1 px-3'>
					<Outlet />
				</main>
				{/* <div className='w-fixed w- flex-shrink flex-grow-0'>
					<div className='flex sm:flex-col px-2'>
						<div className='bg-gray-50 rounded-md border mb-3 w-full'>
							<div className='max-w-sm mx-auto py-8 px-4 sm:px-6 lg:py-12 lg:px-8 lg:flex lg:items-center lg:justify-between'>
								<h2 className='text-lg font-extrabold tracking-tight text-gray-900 sm:text-lg'>
									<span className='block text-primary'>
										🥂🐢🧑‍💻🤣🥱🍗🥘🧙‍♀️🧚‍♂️💻💾📺📸🧮🍎🫐🫒🍑🍑🍑🍑🍑🍑🍑
									</span>
								</h2>
							</div>
						</div>
					</div>
				</div> */}
			</div>
			{/* <footer className='bg-black mt-auto'>
				<div className='p-5 text-white mx-auto'>
					<h1 className='text-2xl'>Footer</h1>
					<div className='flex'>
						<div className='flex-grow flex flex-col'>
							<a href='/#home'>Boom</a>
							<a href='#'>Boom</a>
							<a href='#'>Boom</a>
							<a href='#'>Boom</a>
						</div>
						<div className='flex-grow flex flex-col'>
							<a href='#'>Boom</a>
							<a href='#'>Boom</a>
							<a href='#'>Boom</a>
							<a href='#'>Boom</a>
						</div>
						<div className='flex-grow flex flex-col'>
							<a href='#'>Boom</a>
							<a href='#'>Boom</a>
							<a href='#'>Boom</a>
						</div>
						<div className='flex-grow flex flex-col'>
							<a href='#'>Boom</a>
							<a href='#'>Boom</a>
							<a href='#'>Boom</a>
							<a href='#'>Boom</a>
						</div>
					</div>{' '}
					*
					<div className='text-right text-xs py-4'>
						<a href=''>&copy;2021 Someco Inc.</a>
					</div>
				</div>
			</footer> */}
		</>
	);
}
