import React from 'react';

interface MessageProps {
    message: string;
}

const Message: React.FC<MessageProps> = ({ message }) => <p>{message}</p>;

export default Message;
