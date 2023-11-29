'use client'; // don't render on the server

import { useState } from 'react';
import { useRouter} from 'next/navigation';

export default function CreateContact() {
    const [lastname, setLastname] = useState('');
    const [firstname, setFirstname] = useState('');
    const [phone, setPhone] = useState('');

    const router = useRouter();

    const create = async () => {
        await fetch('http://127.0.0.1:8090/api/collections/contacts/records', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                lastname,
                firstname,
                phone
            })
        })

        setLastname('');
        setFirstname('');
        setPhone('');

        router.refresh();
    }

    return (
        <form onSubmit={create}>
            <h3>Create a new Contact</h3>

            <input
                type="text"
                placeholder='Last name'
                value={lastname}
                onChange={(event) => setLastname(event.target.value)}
            />

            <input
                type="text"
                placeholder='First name'
                value={firstname}
                onChange={(event) => setFirstname(event.target.value)}
            />
            
            <textarea
                placeholder='Phone number'
                value={phone}
                onChange={(event) => setPhone(event.target.value)}
            />

            <button type='submit'>Create contact</button>
        </form>
    )
}
