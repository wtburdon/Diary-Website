
function Entry(props){
    return <li>{props.entry}</li>
}


function EntryList(props){
    return(
        <ul>
            {props.entries.map( (entry) => {
                return <Entry key={entry} entry={entry} />
            })}
        </ul>
    );
}

function contentPage(){
    const Entries = ['Nov 11', 'Oct 31', 'Oct 24']
    
    return(
        <section>
            <div>
                <div className="border"></div>
                <div>
                <h1>CONTENT</h1>
                <EntryList entries={Entries}/>
                </div>
                <div className="border"></div>
            </div>
        </section>
    );
}

export default contentPage