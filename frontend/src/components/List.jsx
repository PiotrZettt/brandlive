import React from 'react'


function List(props){
      function handleClick(){
    props.deletion(props.id)
  }
    return (
        <div className="candidate">
          <h4>  first_name: {props.first_name} </h4>
          <h4>  last_name: {props.last_name} </h4>
          <h4>  email: {props.email} </h4>
          <h4>  gender: {props.gender} </h4>
          <h4>  age: {props.age} </h4>
          <h4>  phone_number: {props.phone_number} </h4>
          <h4>  location: {props.location} </h4>
          <h4>  photo: {props.photo} </h4>
          <h4>  note: {props.note} </h4>
          <button onClick={handleClick}>Delete</button>
        </div>
    )
  }

export default List;