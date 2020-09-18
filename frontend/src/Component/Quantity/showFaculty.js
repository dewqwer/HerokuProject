import React from 'react';
import '../../CSS/Quantity.css';
import Message from './message';
import _ from 'lodash';


class QuantityPage extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            messages: []
        };
        let app = this.props.db.database().ref('messages');
        app.on('value', snapshot => {
            this.getData(snapshot.val());
        });
    }
    handleClick = () => {
        console.log('this is:', this);
    }
    question() {
        alert("Press any word");
    }
    getData(values) {
        let messagesVal = values;
        let messages = _(messagesVal)
            .keys()
            .map(messageKey => {
                let cloned = _.clone(messagesVal[messageKey]);
                cloned.key = messageKey;
                return cloned;
            }).value();
        this.setState({
            messages: messages
        });
    }
    render() {
        let messageNodes = this.state.messages.map((message) => {
            return (
                <div>
                    <div>
                        <Message
                            msgKey={message.key}
                            message={message.message}
                            db={this.props.db} />
                    </div>
                </div>
            )
        });
        return (
            <div>
                {messageNodes}
            </div>
        );

        // return (
        //     <div className="background" >
        //         <div className="question">
        //             <img width="2%" onClick={this.question} src={Question}></img>
        //         </div>
        //         <div className="block">
        //             <div className="flex-container">
        //                 <div className="flex-container-column">
        //                     <button className="flex-div">คณะวิศวกรรมศาสตร์</button>
        //                 </div>
        //                 <div className="flex-container-column">
        //                     <button className="flex-div-2">คณะเทคโนโลยีสารสนเทศ</button>
        //                 </div>
        //                 <div>
        //                     <img src={Next} width="3%" className="Next"></img>
        //                 </div>
        //             </div>
        //         </div>
        //         <div className="flex-container">
        //             <button className="flex-div-back">ก่อนหน้า</button>
        //             <button className="flex-div-skip">ข้าม</button>
        //         </div>
        //     </div >
        // );
    }
};


export default QuantityPage;