import Navbar from './components/NavBar';
import Stats from './components/Stats';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
// import Home from './components/Home';
// import About from './components/About';
// import Contact from './components/Contact';

export default function App() {
	return (
		<>
			<Navbar />
			<Stats />

			<Router>
				<Switch>
					<Route
						exact
						path='/'
						component={Home}
					/>
					<Route
						path='/about'
						component={About}
					/>
					<Route
						path='/contact'
						component={Contact}
					/>
				</Switch>
			</Router>

			{/* <div className='w-screen grid h-screen place-content-center'>
				<div className='flext justify-center items-center  bg-inherit'>
					<form
						// action="{% url 'index' %}"
						method='POST'
						className='p-10 max-w-lg'>
						{/* {% csrf_token %} *
						<div className=''>
							<h2 className='font-bold text-3xl'>Enter</h2>
							<p className='text-xs'>
								Lorem ipsum dolor sit amet, consectetur
								adipiscing elit, sed do eiusmod tempor
								incididunt.
							</p>
						</div>

						<div className='form-control  w-full'>
							<label
								className='label'
								for='program'>
								<span className='label-text'>
									Program
								</span>
							</label>

							<input
								type='text'
								name='program'
								id='program'
								className='input w-full  input-bordered input-success'
							/>
						</div>

						<div className='form-control w-full '>
							<div>
								<label
									className='label'
									for='year'>
									<span className='label-text'>
										Year enrolled
									</span>
								</label>
								<input
									type='text'
									name='year'
									id='year'
									pattern='\d{4}'
									maxlength='4'
									placeholder='e.g 2023'
									className='input w-full  input-bordered input-success'
								/>
							</div>
						</div>

						<div className='form-control w-full '>
							<label
								className='label'
								for='level'>
								<span className='label-text'>
									Level
								</span>
							</label>
							<input
								type='text'
								name='level'
								id='level'
								className='input w-full  input-bordered input-success'
							/>
						</div>

						<button className={`btn ${loading && 'loading'}`} >Register Now</button>
					</form>
				</div>
			</div> */}
		</>
	);
}
