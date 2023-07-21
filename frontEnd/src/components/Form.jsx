import React from 'react';

export default function Form() {
	function puts() {
		return <input type='text' placeholder='fhfhh' />;
	}

	return <form>{puts()}</form>;
}
