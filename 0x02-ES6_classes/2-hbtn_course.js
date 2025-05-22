#!/usr/bin/node

export default class ALXCourse {
  constructor(name:str, length:int, students:union(array)) {
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name {
    return this._name;
  }

  set name(value) {
    if (value !== string) {
      throw new TypeError('name must be a string');
    }
    return this._name = value;
  }

  get length {
    return this._length;
  }

  set length(value) {
    if (value !== number) {
      throw new TypeError('length must be a number');
    }
    return this._length = value;    
  }

  get students {
    return this._length
  }

  set students(value) {
    if (!Array.isArray(value) || !value.every(s => typeof s === 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
    this._students = value;
  }
}
