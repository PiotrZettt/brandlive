import React from 'react'
import {useState, useEffect} from "react";
import axios from "axios";
import List from "./List"

function Candidate() {

    const [candidates , setNewCandidates] = useState(null)
    const [formCandidate, setFormCandidate] = useState({
      first_name: "",
      last_name: "",
      email: "",
      gender: "",
      age: "",
      phone_number: "",
      location: "",
      photo: "",
      note: "",
    })

    useEffect(() => {
      getCandidates()
        } ,[])

    function getCandidates() {
      axios({
          method: "GET",
          url:"http://127.0.0.1:8000/api/candidates/",
        }).then((response)=>{
          const data = response.data
          setNewCandidates(data)
        }).catch((error) => {
          if (error.response) {
            console.log(error.response);
            console.log(error.response.status);
            console.log(error.response.headers);
            }
        })}

    function createCandidate(event) {
        axios({
          method: "POST",
          url:"http://127.0.0.1:8000/api/candidates/",
          data:{
            first_name: formCandidate.first_name,
            last_name: formCandidate.last_name,
            email: formCandidate.email,
            gender: formCandidate.gender,
            age: formCandidate.age,
            phone_number: formCandidate.phone_number,
            location: formCandidate.location,
            photo: formCandidate.photo,
            note: formCandidate.note,
           }
        })
        .then((response) => {
          getCandidates()
        })

        setFormCandidate(({
          first_name: "",
          last_name: "",
          email: "",
          gender: "",
          age: "",
          phone_number: "",
          location: "",
          photo: "",
          note: "",}))

        event.preventDefault()
    }

    function DeleteCandidate(id) {
        axios({
          method: "DELETE",
          url:`http://127.0.0.1:8000/api/candidates/${id}/`,
        })
        .then((response) => {
          getCandidates()
        })
    }

    function handleChange(event) {
        const {value, name} = event.target
        setFormCandidate(prevCandidate => ({
            ...prevCandidate, [name]: value})
        )}


  return (

     <div className=''>

        <form className="create-candidates">
          <input onChange={handleChange} text={formCandidate.first_name} name="first_name" placeholder="Your first name" value={formCandidate.first_name} />
          <input onChange={handleChange} text={formCandidate.last_name} name="last_name" placeholder="Your last name" value={formCandidate.last_name} />
          <input onChange={handleChange} text={formCandidate.email} name="email" placeholder="Your email address" value={formCandidate.email} />
          <input onChange={handleChange} text={formCandidate.gender} name="gender" placeholder="Your gender" value={formCandidate.gender} />
          <input onChange={handleChange} text={formCandidate.age} name="age" placeholder="Your age" value={formCandidate.age} />
          <input onChange={handleChange} text={formCandidate.phone_number} name="phone_number" placeholder="You phone number" value={formCandidate.phone_number} />
          <input onChange={handleChange} text={formCandidate.location} name="location" placeholder="Your location" value={formCandidate.location} />
          <input onChange={handleChange} text={formCandidate.photo} name="photo" placeholder="Your photo" value={formCandidate.photo} />
          <textarea onChange={handleChange} text={formCandidate.note} name="note" placeholder="About you" value={formCandidate.note} />
          <button onClick={createCandidate}>Create Profile</button>
          <button onClick={createCandidate}>Get All Profiles</button>
        </form>

        { candidates && candidates.map(candidate => <List
        key={candidate.id}
        id={candidate.id}
        first_name={candidate.first_name}
        last_name={candidate.last_name}
        email={candidate.email}
        gender={candidate.gender}
        age={candidate.age}
        phone_number={candidate.phone_number}
        location={candidate.location}
        photo={candidate.photo}
        note={candidate.note}
        deletion ={DeleteCandidate}
        />
        )}

    </div>

  );
}

export default Candidate;