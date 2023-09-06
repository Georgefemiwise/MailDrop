import React, { useState } from 'react';
import { Link } from 'react-router-dom';

export default function Profile() {
	const [editProfile, setEditProfile] = useState(false);

	return (
		<div className='p-5'>
			<div className='flex justify-around w-full gap-10'>
				<div className='w-full'>
					<div className='bg-neutral-focus rounded-md py-5 px-8 my-2 capitalize'>
						<div className='avatar placeholder w-full flex justify-center '>
							<div className='min-w-[8rem] rounded-full bg-neutral-content text-neutral '>
								{/* <img src='/images/stock/photo-1534528741775-53994a69daeb.jpg' /> */}
								<span className='text-xs'>AA</span>
							</div>
						</div>
						<h3 className='label mt-9'>
							<span className='capitalize font-medium'>
								username
							</span>
							Georgewise
						</h3>
						<h3 className='label'>
							<span className='capitalize font-medium'>
								first name
							</span>
							George
						</h3>
						<h3 className='label'>
							<span className='capitalize font-medium'>
								last name
							</span>
							wise
						</h3>
						
						<h3 className='label'>
							<span className='capitalize font-medium'>
								DOB
							</span>
							11/11/1111
						</h3>
					{/* </div>

					<div className='font-medium capitalize my-6'>
						contact
					</div>
					<div className='bg-neutral-focus rounded-md py-5 px-8 my-2'> */}
						<h3 className='label'>
							<span className='capitalize font-medium'>
								phone
							</span>
							1234567890
						</h3>
						<h3 className='label'>
							<span className='capitalize font-medium'>
								email
							</span>
							JohnDoe@gmail.com
						</h3>
						<h3 className='label'>
							<span className='capitalize font-medium'>
								phone
							</span>
							1234567890
						</h3>
					</div>
				</div>



				<div className='w-full'>
					<div className='bg-neutral-focus rounded-md py-5 px-8 my-2 capitalize'>
						<div className='avatar placeholder w-full flex justify-center '>
							<div className='min-w-[8rem] rounded-full bg-neutral-content text-neutral '>
								{/* <img src='/images/stock/photo-1534528741775-53994a69daeb.jpg' /> */}
								<span className='text-xs'>logo</span>
							</div>
						</div>
						<h3 className='label mt-9'>
							<span className='capitalize font-medium'>
								company name
							</span>
							Georgewise
						</h3>
						<h3 className='label'>
							<span className='capitalize font-medium'>
								location
							</span>
							George
						</h3>
						<h3 className='label'>
							<span className='capitalize font-medium'>
								industry
							</span>
							wise
						</h3>
						<h3 className='label'>
							<span className='capitalize font-medium'>
								title
							</span>
							CEO
						</h3>
						
					</div>

					<div className='font-medium capitalize my-6'>
						contact
					</div>
					<div className='bg-neutral-focus rounded-md py-5 px-8 my-2'>
						
						<h3 className='label'>
							<span className='capitalize font-medium'>
								email
							</span>
							JohnDoe@gmail.com
						</h3>
						<h3 className='label'>
							<span className='capitalize font-medium'>
								phone
							</span>
							1234567890
						</h3>
						<h3 className='label'>
							<span className='capitalize font-medium'>
								whatsapp
							</span>
							1234567890
						</h3>
					</div>
				</div>
			</div>
		</div>
	);
}
