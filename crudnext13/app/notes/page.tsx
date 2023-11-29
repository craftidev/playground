import Link from "next/link";
import PocketBase from 'pocketbase';
import styles from './Contacts.module.css';
import CreateContact from "./[id]/CreateContact";

// Next13 export variables for cache behavior
export const dynamic = 'auto',
    dynamicParams = true,
    revalidate = 0,
    fetchCache = 'auto',
    runtime = 'nodejs',
    preferredRegion = 'auto'
;

async function getContacts() {
    const pocketBase = new PocketBase('http://127.0.0.1:8090');
    const data = await pocketBase.collection('contacts').getFullList({
        sort: '-created', perPage: 30
    });

    return data as any[];
}

export default async function ContactsPage() {
    const contacts = await getContacts();

    return (
        <div>
            <h1>Contacts</h1>

            <div className={styles.grid}>
                {contacts?.map(contact => {
                    return <Contact key={contact.id} contact={contact} />;
                })}
            </div>

            <CreateContact />
        </div>
    );
}

function Contact({ contact }: any) {
    const { id, lastname, firstname, phone, created } = contact ||{};
    return (
        <Link href={`/contacts/${id}`}>
            <div className={styles.contact}>
                <h2>{lastname} {firstname}</h2>
                <h5>{phone}</h5>
                <p>{created}</p>
            </div>
        </Link>
    );
}
