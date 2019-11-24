CREATE USER trivia WITH PASSWORD 'pass';
CREATE DATABASE trivia;
GRANT ALL PRIVILEGES ON DATABASE trivia TO trivia;

\connect trivia trivia
create table if not exists categories
(
	id serial not null
		constraint categories_pkey
			primary key,
	type text not null
);
create table if not exists questions
(
	id serial not null
		constraint questions_pkey
			primary key,
	question text not null,
	answer text not null,
	difficulty integer not null,
	category_id integer not null
		constraint category
			references categories
				on update cascade on delete set null
);


\connect postgres postgres
CREATE DATABASE trivia_test TEMPLATE trivia;
GRANT ALL PRIVILEGES ON DATABASE trivia_test TO trivia;


\connect trivia trivia
INSERT INTO public.categories (id, type) VALUES (1, 'Science');
INSERT INTO public.categories (id, type) VALUES (2, 'Art');
INSERT INTO public.categories (id, type) VALUES (3, 'Geography');
INSERT INTO public.categories (id, type) VALUES (4, 'History');
INSERT INTO public.categories (id, type) VALUES (5, 'Entertainment');
INSERT INTO public.categories (id, type) VALUES (6, 'Sports');
INSERT INTO public.questions (id, question, answer, difficulty, category_id) VALUES (5, 'Whose autobiography is entitled ''I Know Why the Caged Bird Sings''?', 'Maya Angelou', 2, 4);
INSERT INTO public.questions (id, question, answer, difficulty, category_id) VALUES (9, 'What boxer''s original name is Cassius Clay?', 'Muhammad Ali', 1, 4);
INSERT INTO public.questions (id, question, answer, difficulty, category_id) VALUES (2, 'What movie earned Tom Hanks his third straight Oscar nomination, in 1996?', 'Apollo 13', 4, 5);
INSERT INTO public.questions (id, question, answer, difficulty, category_id) VALUES (4, 'What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?', 'Tom Cruise', 4, 5);
INSERT INTO public.questions (id, question, answer, difficulty, category_id) VALUES (6, 'What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?', 'Edward Scissorhands', 3, 5);
INSERT INTO public.questions (id, question, answer, difficulty, category_id) VALUES (10, 'Which is the only team to play in every soccer World Cup tournament?', 'Brazil', 3, 6);
INSERT INTO public.questions (id, question, answer, difficulty, category_id) VALUES (11, 'Which country won the first ever soccer World Cup in 1930?', 'Uruguay', 4, 6);
INSERT INTO public.questions (id, question, answer, difficulty, category_id) VALUES (12, 'Who invented Peanut Butter?', 'George Washington Carver', 2, 4);
INSERT INTO public.questions (id, question, answer, difficulty, category_id) VALUES (13, 'What is the largest lake in Africa?', 'Lake Victoria', 2, 3);
INSERT INTO public.questions (id, question, answer, difficulty, category_id) VALUES (14, 'In which royal palace would you find the Hall of Mirrors?', 'The Palace of Versailles', 3, 3);
INSERT INTO public.questions (id, question, answer, difficulty, category_id) VALUES (15, 'The Taj Mahal is located in which Indian city?', 'Agra', 2, 3);
INSERT INTO public.questions (id, question, answer, difficulty, category_id) VALUES (16, 'Which Dutch graphic artist–initials M C was a creator of optical illusions?', 'Escher', 1, 2);
INSERT INTO public.questions (id, question, answer, difficulty, category_id) VALUES (17, 'La Giaconda is better known as what?', 'Mona Lisa', 3, 2);
INSERT INTO public.questions (id, question, answer, difficulty, category_id) VALUES (18, 'How many paintings did Van Gogh sell in his lifetime?', 'One', 4, 2);
INSERT INTO public.questions (id, question, answer, difficulty, category_id) VALUES (19, 'Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?', 'Jackson Pollock', 2, 2);
INSERT INTO public.questions (id, question, answer, difficulty, category_id) VALUES (20, 'What is the heaviest organ in the human body?', 'The Liver', 4, 1);
INSERT INTO public.questions (id, question, answer, difficulty, category_id) VALUES (21, 'Who discovered penicillin?', 'Alexander Fleming', 3, 1);
INSERT INTO public.questions (id, question, answer, difficulty, category_id) VALUES (22, 'Hematology is a branch of medicine involving the study of what?', 'Blood', 4, 1);
INSERT INTO public.questions (id, question, answer, difficulty, category_id) VALUES (23, 'Which dung beetle was worshipped by the ancient Egyptians?', 'Scarab', 4, 4);
