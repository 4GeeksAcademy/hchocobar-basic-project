const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			user: null,  // new "store" to save the username or email
			message: null,
			demo: [{title: "First", background: "white", initial: "white"},
						 {title: "Second", background: "white", initial: "white"}]
		},
		actions: {
			login: async function login(email, password) {
				const options = {
					method: 'POST',
					body: {
						email: email,
						password: password
					}
				};
				const response = await fetch(process.env.BACKEND_URL + '/api/login', options);
				if (response.ok) {
					const result = await response.json();
					localStorage.setItem('jwt', result.access_token);
				} else {
					console.log('Error, login not found')
				}
			},
			logout: function logout() {
				localStorage.removeItem('jwt');
			},
			makeRequestWithJWT: async function makeRequestWithJWT() {
				const options = {
					method: 'POST',
					headers: {
						Authorization: `Bearer ${localStorage.getItem('jwt')}`,
					}
				};
				const response = await fetch(process.env.BACKEND_URL + '/api/protected', options);
				if (response.ok) {
					const result = await response.json();
					return result;
				} else {
					console.log('Error, makeRequestWithJWT not found')
				}
			},
			getMessage: async () => {
				try {
					const response = await fetch(process.env.BACKEND_URL + "/api/hello")
					if (response.ok) {
						const data = await response.json()
						setStore({ message: data.message })
						return data;
					} else {
						console.log(response.status, response.statusText)
					}
				} catch (error) {
					console.log("Error loading message from backend", error)
				}
			},
			exampleFunction: () => {getActions().changeColor(0, "green");}, // Use getActions to call a function within a fuction
			changeColor: (index, color) => {
				const store = getStore(); 	// Get the store
				const demo = store.demo.map((item, i) => {
					if (i === index) { item.background = color; }
					return item;
				});
				setStore({ demo: demo });  // Reset the global store
			}
		}
	};
};


export default getState;
