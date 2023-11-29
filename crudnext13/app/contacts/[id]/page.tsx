import styles from '../Contacts.module.css';

async function getContact(contactId: string) {
    const apiResponse = await fetch(
        `http://127.0.0.1:8090/api/collections/contacts/records/${contactId}`,
        {
            next: { revalidate: 10 },
        }
    );
    const dataJson = await apiResponse.json();

    return dataJson;
}

export default async function ContactPage({ params }: any) {
    const contact = await getContact(params.id);

    return (
        <div>
            <h1>contacts/{contact.id}</h1>
            <div className={styles.contact}>
                <h3>{contact.lastname} {contact.firstname}</h3>
                <h5>{contact.phone}</h5>
                <p>{contact.created}</p>
            </div>
        </div>
    );
}
