export default class HolbertonCourse {
  constructor(name, length, students) {
    this.students = students;
    this.name = name;
    this.length = length;
  }

  set students(students) {
    if (!Array.isArray(students) || students.some((s) => typeof s !== 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
    this._students = students;
  }

  get students() {
    return this._students;
  }

  set length(length) {
    if (typeof length !== 'number') {
      throw TypeError('Length must be a number');
    }
    this._length = length;
  }

  get length() {
    return this._length;
  }

  set name(name) {
    if (typeof name !== 'string') {
      throw TypeError('Name must be a string');
    }
    this._name = name;
  }

  get name() {
    return this._name;
  }
}
