import Link from "next/link";
import PocketBase from 'pocketbase';
import styles from './Notes.module.css';

// Next13 export variables for cache behavior
export const dynamic = 'auto',
    dynamicParams = true,
    revalidate = 0,
    fetchCache = 'auto',
    runtime = 'nodejs',
    preferredRegion = 'auto'
;

async function getNotes() {
    // const apiResponse = await fetch(
    //     'http://127.0.0.1:8090/api/collections/notes/records?page=1&perPage=30',
    //     { cache: 'no-store' }
    // );
    // const dataJson = await apiResponse.json();
    const pocketBase = new PocketBase('http://127.0.0.1:8090');
    const data = await pocketBase.collection('notes').getFullList({
        sort: '-created', perPage: 30
    });

    return data as any[];
}

export default async function NotesPage() {
    const notes = await getNotes();
    return (
        <div>
            <h1>Notes</h1>

            <div className={styles.grid}>
                {notes?.map(note => {
                    return <Note key={note.id} note={note} />;
                })}
            </div>
        </div>
    );
}

function Note({ note }: any) {
    const { id, title, content, created } = note ||{};
    return (
        <Link href={`/notes/${id}`}>
            <div className={styles.note}>
                <h2>{title}</h2>
                <h5>{content}</h5>
                <p>{created}</p>
            </div>
        </Link>
    );
}
