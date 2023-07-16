import React from 'react';

import { Outlet } from 'react-router-dom';
import SideBarFrame from './SideBarFrame';

export default function MainFrame() {
	return (
		<>
			<div class='w-full flex flex-col sm:flex-row flex-wrap sm:flex-nowrap py-4 flex-grow h-screen'>
				<SideBarFrame />
				<main role='main' class='w-full flex-grow pt-1 px-3'>
					<Outlet />
				</main>
				<div class='w-fixed w- flex-shrink flex-grow-0 px-2'>
					<div class='flex sm:flex-col px-2'>
						<div class='bg-gray-50 rounded-xl border mb-3 w-full'>
							<div class='max-w-7xl mx-auto py-8 px-4 sm:px-6 lg:py-12 lg:px-8 lg:flex lg:items-center lg:justify-between'>
								<h2 class='text-lg font-extrabold tracking-tight text-gray-900 sm:text-lg'>
									<span class='block text-primary'>
										Made with Tailwind CSS!
									</span>
								</h2>
							</div>
						</div>
					</div>
				</div>
			</div>
			{/* <footer class='bg-black mt-auto'>
				<div class='p-5 text-white mx-auto'>
					<h1 class='text-2xl'>Footer</h1>
					{/* <div class='flex'>
						<div class='flex-grow flex flex-col'>
							<a href='/#home'>Boom</a>
							<a href='#'>Boom</a>
							<a href='#'>Boom</a>
							<a href='#'>Boom</a>
						</div>
						<div class='flex-grow flex flex-col'>
							<a href='#'>Boom</a>
							<a href='#'>Boom</a>
							<a href='#'>Boom</a>
							<a href='#'>Boom</a>
						</div>
						<div class='flex-grow flex flex-col'>
							<a href='#'>Boom</a>
							<a href='#'>Boom</a>
							<a href='#'>Boom</a>
						</div>
						<div class='flex-grow flex flex-col'>
							<a href='#'>Boom</a>
							<a href='#'>Boom</a>
							<a href='#'>Boom</a>
							<a href='#'>Boom</a>
						</div>
					</div> *
					<div class='text-right text-xs py-4'>
						<a href=''>&copy;2021 Someco Inc.</a>
					</div>
				</div>
			</footer> */}
		</>
	);
}
