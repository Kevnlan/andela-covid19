def estimateDays(periodType,timeToElapse):
  if periodType == 'days':
    days = timeToElapse
  elif periodType == 'weeks':
    days = timeToElapse * 7
  elif periodType == 'months':
    days = timeToElapse * 30

  return days


def estimator(data):
  days = estimateDays(data['periodType'],data['timeToElapse'])

  reportedCases = data['reportedCases']


  #Currently Infected
  currentlyInfected = reportedCases * 10
  currentlyInfectedSevere = reportedCases * 50

  #Infections by requested time
  infectionsByRequestedTime = currentlyInfected * \
        (2 ** int(days/3))
  infectionsByRequestedTimeSevere = currentlyInfectedSevere * \
        (2 ** int(days/3))

  severeCasesByRequestedTime = \
        int(0.15 * infectionsByRequestedTime)
  severeCasesByRequestedTimeSevere = \
        int(0.15 * infectionsByRequestedTimeSevere)

  availableBeds = (0.35 * data["totalHospitalBeds"])

  hospitalBedsByRequestedTime = \
        int(availableBeds - severeCasesByRequestedTime)
  hospitalBedsByRequestedTimeSevere = \
        int(availableBeds - severeCasesByRequestedTimeSevere)

  casesForICUByRequestedTimeImpact = \
        int(0.05 * infectionsByRequestedTime)
  casesForICUByRequestedTimeSevere = \
        int(0.05 * infectionsByRequestedTimeSevere)

  casesForVentilatorsByRequestedTimeImpact = \
        int(0.02 * infectionsByRequestedTime)
  casesForVentilatorsByRequestedTimeSevere = \
        int(0.02 * infectionsByRequestedTimeSevere)
  dollarsInFlightImpact = \
        int((infectionsByRequestedTime *
            data["region"]["avgDailyIncomePopulation"] *
            data["region"]["avgDailyIncomeInUSD"]) / days)
  dollarsInFlightSevere = \
        int((infectionsByRequestedTimeSevere *
            data["region"]["avgDailyIncomePopulation"] *
            data["region"]["avgDailyIncomeInUSD"]) / days)

  output = {
      "data": data,
      "impact": {
          "currentlyInfected": currentlyInfected,
          "infectionsByRequestedTime": infectionsByRequestedTime,
          "severeCasesByRequestedTime": severeCasesByRequestedTime,
          "hospitalBedsByRequestedTime": hospitalBedsByRequestedTime,
          "casesForICUByRequestedTime": casesForICUByRequestedTimeImpact,
          "casesForVentilatorsByRequestedTime": casesForVentilatorsByRequestedTimeImpact,
          "dollarsInFlight": dollarsInFlightImpact},
      "severeImpact": {
          "currentlyInfected": currentlyInfectedSevere,
          "infectionsByRequestedTime": infectionsByRequestedTimeSevere,
          "severeCasesByRequestedTime": severeCasesByRequestedTimeSevere,
          "hospitalBedsByRequestedTime": hospitalBedsByRequestedTimeSevere,
          "casesForICUByRequestedTime": casesForICUByRequestedTimeSevere,
          "casesForVentilatorsByRequestedTime": casesForVentilatorsByRequestedTimeSevere,
          "dollarsInFlight": dollarsInFlightSevere}
  }

  return output

