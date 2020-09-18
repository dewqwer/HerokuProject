import React, { Component } from 'react';
import FacultyBox from './addFaculty';
import FacultyList from './showFaculty';
import firebase from 'firebase';

import QuestionIcon from '../../IMG/Icons/Question.png';
import NextIcon from '../../IMG/Icons/Next.png';

class Quantity extends Component {
    constructor(props) {
        super(props); var firebaseConfig = {
            apiKey: "AIzaSyCgerCkI1mr7e07xWQzKP4NVyB9oC3XwU4",
            authDomain: "senior-fai.firebaseapp.com",
            databaseURL: "https://senior-fai.firebaseio.com",
            projectId: "senior-fai",
            storageBucket: "senior-fai.appspot.com",
            messagingSenderId: "862530252379",
            appId: "1:862530252379:web:8be01dd78daa026dee997e",
            measurementId: "G-YBP3PN9PEF"
        };
        if (!firebase.apps.length) {
            firebase.initializeApp(firebaseConfig);
            firebase.analytics();
        }
    }
    render() {
        return (
            <div className="background">
                <div className="question">
                    <img width="2%" onClick={this.question} src={QuestionIcon}></img>
                </div>
                <div className="block">
                    <div className="flex-container">
                        <div className="flex-container-column">
                            <button className="flex-div"><FacultyList db={firebase} /></button>
                            <button className="flex-div"><FacultyList db={firebase} /></button>
                            <button className="flex-div"><FacultyList db={firebase} /></button>
                            <button className="flex-div"><FacultyList db={firebase} /></button>
                        </div>
                        <div className="flex-container-column">
                            <button className="flex-div-2"><FacultyList db={firebase} /></button>
                        </div>
                        <div>
                            <img src={NextIcon} width="3%" className="Next"></img>
                        </div>
                    </div>
                </div>
                <div>
                    <div>
                        <FacultyBox db={firebase} />
                    </div>
                </div>
            </div>
        );
    };
}


export default Quantity;