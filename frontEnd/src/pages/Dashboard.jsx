export default function Dashboard() {
	return (
		<div>
			<div className='nav w-full my-5'>
				<ul className='flex gap-2 justify-center capitalize'>
					<li>
						<a className='cursor-pointer '>home</a>
					</li>
					<li>
						<a className='cursor-pointer '>
							sendsmsg{/* The button to open modal */}
							<label htmlFor='man' className='btn btn-xs'>
								details
							</label>
							{/* Put this part before </body> tag */}
							<input
								type='checkbox'
								id='man'
								className='modal-toggle'
							/>
						</a>
					</li>
					<li>
						<a className='cursor-pointer '>profile</a>
					</li>
				</ul>
			</div>
			<div className='flex flex-row'>
				<div className='modal'>
					<div className='modal-box p-10'>
						<div className='modal-action'>adadelta
							<label htmlFor='kingman' className='btn'>
								Close!
							</label>
						</div>
					</div>
				</div>
				<form action='' className='w-96 gap-2 flex flex-col'>
					<div className='form-control'>
						<input
							type='text'
							className='input input-bordered w-full max-w-sm'
							name='to'
							id='to'
							placeholder='To'
						/>
					</div>
					<div className='form-control'>
						<input
							className='input input-bordered w-full max-w-sm'
							type='text'
							name='subject'
							id='subject'
							placeholder='subject'
						/>
					</div>
					<div className='form-control '>
						<textarea
							placeholder='Bio'
							className='textarea textarea-bordered textarea-lg h-56 w-full max-w-sm'></textarea>
					</div>
				</form>
			</div>
		</div>
	);
}
