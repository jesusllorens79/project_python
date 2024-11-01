# Un programa python 
from src.student.student import *
from data_schema.test_data_schema import INPUT_SCHEMA

def orchestrator(args, env_paths, logger):
    """
    :param logger: This is for logging the events
    :return  student_df: Returns all the transformation applied to the studnt records
    Obj: The main purposes is to teach how we can program
    """
    # Crear un objeto de CD
    CD_student  = studentCD(name=args.student, age=args.age, logger=logger)
    CD_student.print_data()

    ADE_student = studentADE(name=args.student, age=args.age, logger=logger)
    ADE_student.print_data()

    # Leer DataFrame

    logger.logger.log(logging.INFO, "Input Path " + str(INPUT_SCHEMA.NAME.value))

