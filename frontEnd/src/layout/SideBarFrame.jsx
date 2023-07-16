import React from 'react';

import NavBar from '../components/Navigation/NavBar'
export default function SideBarFrame() {
	return (
		<aside className=' bg-slate-100 min-w-[10rem] p-1'>
			<div class='w- min-w-fit flex-shrink flex-grow-0 px-4  flex justify-between'>
				<div class='sticky top-0 p-4 bg-gray-100  w-full h-full'>
					{/* <ul class='flex sm:flex-col overflow-hidden content-center justify-center'>
							<li class='py-2 hover:bg-indigo-300 rounded'>
								<a class='truncate' href='#'>
									<img
										src='//cdn.jsdelivr.net/npm/heroicons@1.0.1/outline/home.svg'
										class='w-7 sm:mx-2 mx-4 inline'
									/>
									<span class='hidden sm:inline'>
										Home
									</span>
								</a>
							</li>
							<li class='py-2 hover:bg-indigo-300 rounded'>
								<a class='truncate' href='#'>
									<img
										src='//cdn.jsdelivr.net/npm/heroicons@1.0.1/outline/cog.svg'
										class='w-7 sm:mx-2 mx-4 inline'
									/>{' '}
									<span class='hidden sm:inline'>
										Settings
									</span>
								</a>
							</li>
							<li class='py-2 hover:bg-indigo-300 rounded'>
								<a class='' href='#'>
									<img
										src='//cdn.jsdelivr.net/npm/heroicons@1.0.1/outline/gift.svg'
										class='w-7 sm:mx-2 mx-4 inline'
									/>{' '}
									<span class='hidden sm:inline'>
										Products
									</span>
								</a>
							</li>
							<li class='py-2 hover:bg-indigo-500 rounded'>
								<a class='' href='#'>
									<img
										src='//cdn.jsdelivr.net/npm/heroicons@1.0.1/outline/chart-bar.svg'
										class='w-7 sm:mx-2 mx-4 inline'
									/>{' '}
									<span class='hidden sm:inline'>
										Reports
									</span>
								</a>
							</li>
							<li class='py-2 hover:bg-indigo-300 rounded'>
								<a class='' href='#'>
									<img
										src='//cdn.jsdelivr.net/npm/heroicons@1.0.1/outline/collection.svg'
										class='w-7 sm:mx-2 mx-4 inline'
									/>{' '}
									<span class='hidden sm:inline'>
										Integrations
									</span>
								</a>
							</li>
						</ul> */}

					<NavBar />
				</div>
			</div>
		</aside>
	);
}
