/* eslint-disable */
// Unit Test Code:
describe('control', () => {
  let producao;
  let control;
  let statistics;

  beforeEach(() => {
    producao = document.createElement('input');
    producao.id = 'producao';

    control = [{ dataset: { control: '-', part: 'bracos' } }, { dataset: { control: '+', part: 'blindagem' } }];

    statistics = [{ dataset: { statistic: 'forca' }, textContent: 0 }, { dataset: { statistic: 'poder' }, textContent: 0 }];
  });

  it('should call manipulateCount with the correct arguments when clicked', () => {
    const spy = jest.spyOn(global, 'manipulateCount');

    handleAlertEvent({ type: 'click' });

    expect(spy).toHaveBeenCalledWith('-', control[0]);
  });

  it('should call updateStatistics with the correct arguments when clicked', () => {
    const spy = jest.spyOn(global, 'updateStatistics');

    handleAlertEvent({ type: 'click' });

    expect(spy).toHaveBeenCalledWith('bracos', '-');
  });

  it('should call sayHi2 when clicked', () => {
    const spy = jest.spyOn(global, 'sayHi2');

    handleAlertEvent({ type: 'click' });

    expect(spy).toHaveBeenCalled();
  });

  it('should call changeButtonValue when clicked', () => {
    const spy = jest.spyOn(global, 'changeButtonValue');

    handleAlertEvent({ type: 'click' });

    expect(spy).toHaveBeenCalled();
  });
});
