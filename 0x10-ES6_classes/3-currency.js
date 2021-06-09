export default class Currency {
  constructor(name, code) {
    this.name = name;
    this.code = code;
  }

  get code() {
    return this._code;
  }

  set code(code) {
    this._code = code;
  }

  get name() {
    return this._name;
  }

  set name(name) {
    this._name = name;
  }

  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}
