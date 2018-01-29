import * as indexModule from './index';
import {throws, loop} from './index'
import errorFunction from './errorFunction'
import { add } from './add'
import * as addModule from './add'
import request from 'supertest';
import mongoose from 'mongoose';

let mongoServer;
let server;

jest.mock('./errorFunction');
errorFunction.mockImplementation();

beforeAll(() => {

})

describe('index', () => {
  describe('add function', () => {
    test('1 plus 1', () => {
      var two = add(1,1);
      expect(two).toBe(2);
    });
    test('null plus 1', () => {
      var one = add(null, 1);
      expect(one).toBe(1);
    });
    test('null', () => {
      var zero = add();
      expect(zero).toBeNaN();
    });
  });

  describe('Error function', () => {
    test('Throw Error', () => {
      const ErrorSpy = jest.spyOn(indexModule, 'throws');
      throws();
      throws();
      throws();
      expect(ErrorSpy).toHaveBeenCalledTimes(3);
    });
  });

  describe('loop Function', () => {
    test('Call N times', () => {
      const addSpy = jest.spyOn(addModule, 'add');
      loop(5);
      expect (addSpy).toHaveBeenCalledTimes(5);
    })
  })
});
