import React from 'react'

const StaticGraph = () => {
    const html = '<div><h1>Hello world!</h1><p>This is some static HTML.</p></div>';
    return <div dangerouslySetInnerHTML={{ __html: html }}/>;
  }

export default StaticGraph;