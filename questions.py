"""
This module contains the questions for the Dragaera House Quiz.
Each question is represented as a dataclass containing the title,
descriptive text, and possible choices.
"""
from dataclasses import dataclass, field, fields
from typing import TypeAlias

from cycle import TheCycle


AnswerScores: TypeAlias = list[float, float, float]
Answer: TypeAlias = float

@dataclass(kw_only=True, slots=True)
class Question:
    """Class for storing a single quiz question."""
    title: str
    text: str
    choices: list[str, str, str]


@dataclass(kw_only=True, slots=True)
class QuestionNames:
    """Class containing all questions in the quiz."""
    Enchantress: Question | Answer | AnswerScores
    Court: Question | Answer | AnswerScores
    Duel: Question | Answer | AnswerScores
    Jhereg: Question | Answer | AnswerScores
    Phoenix: Question | Answer | AnswerScores
    Uprising: Question | Answer | AnswerScores
    Athyra: Question | Answer | AnswerScores
    Iorich: Question | Answer | AnswerScores
    Lyorn: Question | Answer | AnswerScores
    Yendi: Question | Answer | AnswerScores
    Oracle: Question | Answer | AnswerScores
    Issola: Question | Answer | AnswerScores
    Vallista: Question | Answer | AnswerScores
    Dragon: Question | Answer | AnswerScores
    Chreotha: Question | Answer | AnswerScores
    Tsalmoth: Question | Answer | AnswerScores
    Jhegaala: Question | Answer | AnswerScores

    def keys(self) -> list[str]:
        return [field.name for field in fields(self) if not field.name.startswith('_')]

    def items(self) -> list[tuple[str, Question | Answer | AnswerScores]]:
        return [(key, getattr(self, key)) for key in self.keys()]

    def __getitem__(self, key: str | int) -> Question | Answer | AnswerScores:
        if isinstance(key, int):
            key = self.keys()[key]
        return getattr(self, key)

    def __len__(self) -> int:
        return len(self.keys())


Answers = QuestionNames


@dataclass(kw_only=True, slots=True)
class Questions(QuestionNames):
    _current_question: int = field(default=-1, init=False, repr=False)

    def next_question(self) -> Question | Answer | None:
        """Return the next question, or None if there are no more questions."""
        if self._current_question < len(self) - 1:
            self._current_question += 1
            question = self[self._current_question]
            return question
        return None

    def previous_question(self) -> Question | Answer | None:
        """Return the previous question, or None if at the beginning."""
        if self._current_question > 0:
            self._current_question -= 1
            question = self[self._current_question]
            return question
        return None

    def reset(self) -> None:
        """Reset to the first question."""
        self._current_question = 0

    @property
    def current_index(self) -> int:
        """Return the current question index."""
        return self._current_question

    @property
    def current_key(self) -> str:
        """Return the current question key."""
        return self.keys()[self._current_question]



def get_questions() -> Questions:
    """Return the questions for the quiz."""
    return Questions(
        Enchantress=Question(
            title="The Affair of the Enchantress's Hospitality",
            text="It has come to your attention—through means which we shall not examine too closely, lest we become entangled in matters of Sources and Discretion—that a certain lady of your acquaintance has been, shall we say, invited rather insistently to the fortress of Dzur Mountain. The Enchantress of Dzur Mountain, whose reputation in matters of sorcery and longevity requires no elaboration from this historian, has extended what some might call hospitality and others might term captivity. The lady's family, it must be noted, has offered a considerable reward for her retrieval.",
            choices=[
                "Assemble a band of worthy companions and ascend to Dzur Mountain forthwith, for a true hero does not calculate odds when honor and a lady's freedom hang in the balance",
                "Request a formal audience with the Enchantress through proper channels, for she is known to respect protocol and may be persuaded through reasoned discourse",
                "Investigate the circumstances more thoroughly before acting, for the Enchantress rarely acts without cause, and understanding her motivations may prove more valuable than hasty rescue"
            ]
        ),
        Court=Question(
            title="The Question of Advancement Within the Court",
            text="You find yourself, dear reader, positioned mere steps from a seat on the Imperial Council—a position which, as Any student of the Cycle will acknowledge, carries with it influence both considerable and consequential. Three paths present themselves to secure this final advancement, each with its advocates among those whose counsel you have sought, and each presenting a rather different approach to the matter of personal elevation.",
            choices=[
                "Challenge the current Council member to formal combat, for nothing demonstrates worthiness for high position more clearly than martial prowess publicly displayed",
                "Cultivate alliances through careful diplomacy and strategic favors, building a network of obligations that will secure support when the moment arrives",
                "Focus on performing your current duties with such excellence that advancement becomes inevitable, trusting merit to speak louder than ambition"
            ]
        ),
        Duel=Question(
            title="The Incident of the Sorcerous Duel",
            text="A rival practitioner of the Art—for so we must call sorcery when speaking of those who have studied it formally—has challenged you to a duel of magical prowess before an audience of your peers. The challenge stems from a disagreement regarding theoretical principles which, while intellectually significant, hardly seems worth mortal danger. Yet to decline would be to concede the argument and suffer considerable damage to one's scholarly reputation.",
            choices=[
                "Accept immediately and prepare your most devastating spells, for in matters of Art as in matters of blade, hesitation is defeat",
                "Accept but propose strict limitations on the duel to minimize danger while still allowing a clear demonstration of superior technique",
                "Decline the duel but publish a detailed treatise dismantling your rival's theories, winning the argument through scholarship rather than spectacle"
            ]
        ),
        Jhereg=Question(
            title="The Mystery of the Jhereg's Proposal",
            text="A representative of the Organization—which is to say, a member of House Jhereg engaged in those commercial enterprises we shall tactfully decline to specify—approaches you with a business proposition. The venture is, we must acknowledge, likely to be profitable beyond ordinary measure, and the Jhereg assures you that your role would be entirely legitimate, serving merely as a respectable face for the enterprise. Your involvement would require neither knowledge of nor participation in Any of the venture's less savory aspects.",
            choices=[
                "Accept the proposal, for gold is gold regardless of its source, and maintaining willful ignorance of details is a time-honored tradition among the nobility",
                "Decline politely but firmly, for association with the Jhereg, however profitable, inevitably leads to complications that no amount of wealth can remedy",
                "Express interest but insist on knowing every detail of the operation before committing, for entering Any arrangement blindly is the mark of a fool"
            ]
        ),
        Phoenix=Question(
            title="The Predicament of the Phoenix Heir",
            text="The current Cycle approaches its end, and a young Phoenix—heir to a distinguished lineage—seeks your counsel on how best to prepare for the rising of their House to Imperial power. This Phoenix, whose sincerity is evident even if their practical experience is limited, asks whether they should spend these final years in military service, scholarly study, or traveling the Empire to understand its peoples. Your advice, it seems, will significantly influence their path.",
            choices=[
                "Recommend military service, for leaders must understand strategy, command, and the realities of warfare if they are to rule effectively",
                "Suggest scholarly pursuits, for knowledge of history, law, and sorcery forms the foundation of wise governance",
                "Advise extensive travel and observation, for understanding the Empire's diverse peoples and their needs is worth more than Any amount of book learning"
            ]
        ),
        Uprising=Question(
            title="The Affair of the Teckla Uprising",
            text="In a province adjacent to your own holdings, the Teckla have risen in revolt—not, we must note, against the Empire itself, but against certain local practices of taxation and labor obligation which they claim exceed both law and custom. The local Dragon lord has requested your assistance in suppressing this disorder, yet you have also received a petition from the Teckla themselves, presenting their grievances with surprising eloquence and citing specific Imperial precedents.",
            choices=[
                "Support the Dragon lord immediately with troops, for regardless of the merit of grievances, rebellion against lawful authority cannot be tolerated",
                "Offer to mediate the dispute, investigating the Teckla's claims and attempting to negotiate a settlement that addresses legitimate grievances",
                "Decline involvement entirely, for the matter lies outside your jurisdiction and interference in a neighboring lord's affairs sets dangerous precedents"
            ]
        ),
        Athyra=Question(
            title="The Question of the Experimental Sorcery",
            text="An Athyra colleague has developed a sorcerous technique that could, if successful, allow direct observation of events from the past—not through historical record, but through actual temporal viewing. The potential for historical scholarship is revolutionary; however, the experiment requires a test subject, and there exists a non-trivial possibility that said subject might become temporarily lost in time. Your colleague, with admirable directness, asks if you would volunteer.",
            choices=[
                "Volunteer enthusiastically, for the advancement of knowledge justifies considerable personal risk, and what glory to be the first to achieve such a feat!",
                "Decline to participate personally but offer to help recruit other volunteers and provide resources for the experiment",
                "Attempt to dissuade your colleague from the experiment entirely, for tampering with time seems likely to produce consequences far beyond Anyone's ability to predict or control"
            ]
        ),
        Iorich=Question(
            title="The Incident at the Iorich Court",
            text="You have been called to testify in a trial where a defendant, whom you believe to be innocent based on your personal knowledge of their character, faces conviction due to circumstantial evidence that appears damning. You possess no concrete evidence of their innocence, only your strong personal conviction. The Iorich presiding has made clear they will accept only factual testimony, not character references or personal opinions.",
            choices=[
                "Testify honestly within the court's constraints, presenting only facts and accepting that justice must follow proper procedure even if the outcome troubles you",
                "Find a way to present your conviction of their innocence persuasively while remaining technically within the court's guidelines, using rhetoric to sway opinion",
                "Refuse to testify at all rather than participate in what you believe will be a miscarriage of justice, and instead work outside the court to prove the defendant's innocence"
            ]
        ),
        Lyorn=Question(
            title="The Dilemma of the Lyorn Succession",
            text="A distant relative, whose claim to your House's ancient seat is technically superior to your own by the strictest interpretation of traditional succession law, has emerged after years abroad and formally asserted their right to the title you currently hold. Your own claim rests on continuous residence, active stewardship, and the support of those who have known you as their lord for decades. The matter must be resolved, and the Lyorn Council awaits your decision on how to proceed.",
            choices=[
                "Acknowledge their superior claim immediately and cede the title with grace, for tradition and law must supersede personal attachment or practical considerations",
                "Contest the claim through every legal means available, for active stewardship and earned loyalty should weigh more heavily than bloodline technicalities",
                "Propose a compromise where you retain the title for your lifetime with succession passing to your relative, honoring both tradition and present reality"
            ]
        ),
        Yendi=Question(
            title="The Matter of the Yendi's Game",
            text="You have discovered that you are—and indeed, have been for some months—an unwitting piece in an elaborate political maneuver orchestrated by a Yendi master of intrigue. Several of your recent decisions, made for what seemed excellent reasons at the time, have apparently advanced this Yendi's agenda in ways you had not perceived. The scheme appears to involve no direct harm to you, but neither does it serve your interests. Most intriguingly, the Yendi has now revealed their manipulation to you directly, apparently curious to see how you will respond.",
            choices=[
                "Confront the Yendi directly and demand compensation for having been manipulated, for none should presume to use another as an unwitting tool",
                "Study the Yendi's methods carefully and attempt to turn the situation to your own advantage, for what better education in intrigue than this?",
                "Withdraw from the situation entirely and restructure your affairs to be less vulnerable to such manipulation in future, considering the experience a valuable lesson"
            ]
        ),
        Oracle=Question(
            title="The Circumstance of the Oracle's Prophecy",
            text="You have consulted an oracle of considerable reputation regarding a significant decision—whether to commit your forces to a military campaign whose success would bring great glory but whose failure would mean ruin. The oracle's prophecy, delivered in characteristic ambiguity, can be interpreted in two equally plausible ways: either as promising victory if you show courage, or as warning of disaster if you show recklessness. The oracle, when pressed for clarification, merely smiled and suggested that distinguishing courage from recklessness is itself the test.",
            choices=[
                "Commit to the campaign, interpreting the prophecy as a promise of victory for the bold, for oracles speak truth to those with courage to seize destiny",
                "Decline the campaign, for the oracle's ambiguity itself serves as warning that the venture's risks outweigh its potential rewards",
                "Proceed with the campaign but with careful planning and fallback positions, neither wholly trusting nor wholly dismissing the prophecy"
            ]
        ),
        Issola=Question(
            title="The Question of the Issola's Request",
            text="An Issola diplomat, whose courtesy is matched only by their effectiveness in delicate negotiations, requests your assistance in a matter of considerable sensitivity. Two powerful Houses stand on the brink of a conflict that could draw in half the Empire, and the Issola believes that you, specifically, possess the unique combination of relationships and reputation necessary to mediate. However, success would require weeks of your time, involve substantial personal risk, and offer no direct benefit to yourself or your House beyond the satisfaction of having prevented bloodshed.",
            choices=[
                "Accept immediately, for the opportunity to prevent widespread conflict is itself sufficient reward, and service to the Empire transcends personal interest",
                "Decline politely, for you have responsibilities to your own House that must take precedence over involving yourself in others' disputes, however noble the cause",
                "Accept on the condition that the Issola secures formal recognition and compensation for your service, for even selfless acts deserve acknowledgment"
            ]
        ),
        Vallista=Question(
            title="The Affair of the Vallista's Commission",
            text="A Vallista architect of exceptional talent has designed a revolutionary bridge that would connect two portions of the Empire currently separated by treacherous mountain passes, reducing a journey of weeks to one of mere days. However, the construction would require demolishing a small but ancient monastery that holds significant historical value. The monks are willing to relocate if the Empire deems it necessary, but the decision falls to you as the local authority. The Vallista's design cannot be modified to preserve the structure.",
            choices=[
                "Approve the bridge's construction, for the living should not be held hostage to the past, and the practical benefit to thousands outweighs sentiment for old stones",
                "Refuse the project, for some things once destroyed cannot be replaced, and the Empire possesses sufficient roads without sacrificing its heritage",
                "Commission a thorough documentation of the monastery before its demolition and ensure its treasures are preserved, attempting to honor both progress and history"
            ]
        ),
        Dragon=Question(
            title="The Incident of the Dragon's Challenge",
            text="During a formal gathering, a Dragon noble—whose reputation for martial prowess is exceeded only by their reputation for arrogance—publicly declares that your House has grown soft and irrelevant in the current Cycle, suggesting that none of your generation would survive a day in actual combat. This pronouncement is clearly intended to provoke a response, and the assembled nobles await your reaction with considerable interest. To ignore the slight would seemingly confirm it; to respond might play directly into the Dragon's hands.",
            choices=[
                "Challenge the Dragon to immediate combat, for such insults cannot be tolerated and must be answered with steel regardless of the challenger's evident skill",
                "Respond with cutting wit that undermines the Dragon's credibility without requiring violence, demonstrating that cleverness is itself a form of strength",
                "Ignore the provocation entirely with deliberate, obvious disdain, for acknowledging such transparent attempts at manipulation only grants them importance they do not merit"
            ]
        ),
        Chreotha=Question(
            title="The Mystery of the Chreotha's Hunt",
            text="You have been invited to join a Chreotha noble on a hunt for a creature that, according to rumor, should not exist—some speak of a dzur of unusual size and intelligence, while others whisper of something far stranger. The Chreotha claims to have tracked this creature for months and believes it represents either a significant zoological discovery or a dangerous predator that threatens nearby settlements. The hunt will be arduous and possibly dangerous, but the Chreotha's enthusiasm is infectious, and their tracking skills are undeniable.",
            choices=[
                "Join the hunt eagerly, for the pursuit of mystery and the test of skill against a worthy opponent is its own reward, regardless of practical benefit",
                "Decline the invitation, for chasing rumors into wilderness seems an inefficient use of time when genuine responsibilities await at home",
                "AccompAny the hunt but focus on observing and documenting rather than participating in the kill, for understanding the creature matters more than slaying it"
            ]
        ),
        Tsalmoth=Question(
            title="The Predicament of the Tsalmoth's Bargain",
            text="A Tsalmoth merchant offers you an arrangement whereby you would provide your name and rank as endorsement for their enterprise—a perfectly legitimate trading compAny—in exchange for a percentage of profits. The merchant is honest about the enterprise's modest prospects and significant competition, but believes your association would provide the credibility necessary to attract investors. The arrangement would require minimal effort on your part but would permanently link your reputation to the compAny's fortunes, whether favorable or otherwise.",
            choices=[
                "Accept the arrangement, for passive income from legitimate enterprise is sensible, and supporting commerce benefits the Empire broadly",
                "Decline, for tying one's reputation to another's business creates vulnerabilities and obligations that no amount of profit justifies",
                "Propose becoming a silent investor instead, providing capital rather than endorsement, thus sharing in potential rewards while limiting reputational risk"
            ]
        ),
        Jhegaala=Question(
            title="The Question of the Jhegaala's Transformation",
            text="You encounter a Jhegaala who claims to have recently undergone the transformation for which their House is known—abandoning their previous identity entirely to assume a new name, profession, and place in society. They reveal this to you because, in their previous life, you owed them a substantial debt that remains legally valid. However, Jhegaala tradition holds that such debts are voided by transformation, as the creditor no longer exists in Any meaningful sense. The Jhegaala seems genuinely curious whether you will honor the legal obligation or respect their House's tradition.",
            choices=[
                "Pay the debt in full, for legal obligations transcend personal transformation, and one cannot escape responsibility through deliberate reinvention",
                "Refuse payment, for respecting House Jhegaala's traditions regarding transformation is itself a form of obligation, and they have chosen to embrace that tradition",
                "Offer to pay as much of the money as they choose to a cause of their own volition, acknowledging both the legal claim and the tradition's significance, and proposing this compromise as honoring both principles"
            ]
        )
    )


def get_answers() -> TheCycle:
    """Return the answers associated with each question."""
    return TheCycle(
        Phoenix=Questions(
            Enchantress=[1, 0, 1],
            Court=[-1, 0, 1],
            Duel=[-1, 1, 1],
            Jhereg=[-1, 1, 0],
            Phoenix=[0, 1, 1],
            Uprising=[-1, 1, 0],
            Athyra=[1, 0, -1],
            Iorich=[0, 1, 1],
            Lyorn=[1, 0, 1],
            Yendi=[1, 0, 1],
            Oracle=[1, 0, 1],
            Issola=[0, -1, 1],
            Vallista=[1, -1, 0],
            Dragon=[1, -1, 0],
            Chreotha=[0, -1, 1],
            Tsalmoth=[0, -1, 1],
            Jhegaala=[1, -1, 1],
        ),
        Dragon=Questions(
            Enchantress=[1, 0, 0],
            Court=[1, 0, 0],
            Duel=[1, 0, -1],
            Jhereg=[-1, 1, 0],
            Phoenix=[1, 0, 0],
            Uprising=[1, 0, -1],
            Athyra=[-1, 0, 1],
            Iorich=[1, 0, 0],
            Lyorn=[0, 1, 0],
            Yendi=[1, 0, 0],
            Oracle=[1, 0, 0],
            Issola=[1, 0, 0],
            Vallista=[0, 1, 0],
            Dragon=[1, 0, 0],
            Chreotha=[1, 0, 0],
            Tsalmoth=[1, -1, 0],
            Jhegaala=[1, -1, 0],
        ),
        Lyorn=Questions(
            Enchantress=[0, 1, 1],
            Court=[0, 1, 1],
            Duel=[-1, 1, 0],
            Jhereg=[-1, 1, 0],
            Phoenix=[0, 1, 0],
            Uprising=[1, 1, 0],
            Athyra=[0, 0, 1],
            Iorich=[1, 0, -1],
            Lyorn=[1, 0, 1],
            Yendi=[0, 1, 1],
            Oracle=[1, 0, 1],
            Issola=[0, 0, 1],
            Vallista=[1, -1, 0],
            Dragon=[1, -1, 0],
            Chreotha=[0, 1, 1],
            Tsalmoth=[0, 1, 1],
            Jhegaala=[1, 0, 1],
        ),
        Tiassa=Questions(
            Enchantress=[-1, 0, 1],
            Court=[-1, 0, 1],
            Duel=[-1, 1, 1],
            Jhereg=[-1, 0, 1],
            Phoenix=[0, 0, 1],
            Uprising=[-1, 1, 0],
            Athyra=[1, 0, -1],
            Iorich=[0, 1, 1],
            Lyorn=[-1, 0, 1],
            Yendi=[0, 1, 1],
            Oracle=[0, 1, 1],
            Issola=[0, -1, 1],
            Vallista=[1, -1, 0],
            Dragon=[0, -1, 1],
            Chreotha=[-1, 1, 0],
            Tsalmoth=[0, -1, 1],
            Jhegaala=[0, -1, 1],
        ),
        Athyra=Questions(
            Enchantress=[-1, 0, 1],
            Court=[-1, 0, 1],
            Duel=[-1, 1, 1],
            Jhereg=[-1, 0, 1],
            Phoenix=[0, 1, 0],
            Uprising=[-1, 1, 0],
            Athyra=[1, 1, -1],
            Iorich=[1, 0, 0],
            Lyorn=[1, 0, 1],
            Yendi=[0, 1, 1],
            Oracle=[0, 1, 1],
            Issola=[-1, 0, 1],
            Vallista=[1, 0, 0],
            Dragon=[-1, 0, 1],
            Chreotha=[-1, 0, 1],
            Tsalmoth=[0, 1, 1],
            Jhegaala=[1, -1, 1],
        ),
        Issola=Questions(
            Enchantress=[-1, 1, 1],
            Court=[-1, 1, 0],
            Duel=[-1, 1, 1],
            Jhereg=[-1, 1, 0],
            Phoenix=[0, 1, 1],
            Uprising=[-1, 1, 0],
            Athyra=[0, 1, -1],
            Iorich=[0, 1, 1],
            Lyorn=[-1, 0, 1],
            Yendi=[-1, 1, 1],
            Oracle=[-1, 1, 0],
            Issola=[-1, 0, 1],
            Vallista=[1, -1, 0],
            Dragon=[0, -1, 1],
            Chreotha=[-1, 1, 0],
            Tsalmoth=[-1, 0, 1],
            Jhegaala=[1, -1, 1],
        ),
        Yendi=Questions(
            Enchantress=[-1, 0, 1],
            Court=[-1, 1, 0],
            Duel=[-1, 0, 1],
            Jhereg=[-1, 0, 1],
            Phoenix=[0, 1, 0],
            Uprising=[-1, 1, 0],
            Athyra=[0, 1, 0],
            Iorich=[0, 1, 1],
            Lyorn=[-1, 0, 1],
            Yendi=[-1, 1, 0],
            Oracle=[-1, 1, 1],
            Issola=[-1, 0, 1],
            Vallista=[0, -1, 1],
            Dragon=[1, 0, 1],
            Chreotha=[-1, 1, 1],
            Tsalmoth=[-1, 0, 1],
            Jhegaala=[0, -1, 1],
        ),
        Jhereg=Questions(
            Enchantress=[-1, 0, 1],
            Court=[-1, 1, 0],
            Duel=[0, 1, 1],
            Jhereg=[1, -1, 1],
            Phoenix=[0, 0, 1],
            Uprising=[0, 1, 0],
            Athyra=[-1, 1, 0],
            Iorich=[0, 1, 1],
            Lyorn=[-1, 1, 0],
            Yendi=[1, 0, 1],
            Oracle=[0, 1, 1],
            Issola=[0, 0, 1],
            Vallista=[-1, 0, 1],
            Dragon=[1, -1, 1],
            Chreotha=[0, -1, 1],
            Tsalmoth=[1, -1, 1],
            Jhegaala=[0, -1, 1],
        ),
        Orca=Questions(
            Enchantress=[-1, 1, 1],
            Court=[-1, 1, 0],
            Duel=[-1, 1, 0],
            Jhereg=[0, -1, 1],
            Phoenix=[0, 0, 1],
            Uprising=[-1, 1, 0],
            Athyra=[0, 1, -1],
            Iorich=[0, 1, 0],
            Lyorn=[-1, 0, 1],
            Yendi=[-1, 1, 0],
            Oracle=[1, 1, 0],
            Issola=[0, -1, 1],
            Vallista=[0, -1, 1],
            Dragon=[1, -1, 0],
            Chreotha=[-1, 0, 1],
            Tsalmoth=[1, 0, 0],
            Jhegaala=[1, -1, 0],
        ),
        Dzur=Questions(
            Enchantress=[1, 0, -1],
            Court=[1, -1, 0],
            Duel=[1, 0, -1],
            Jhereg=[-1, 1, 0],
            Phoenix=[1, 0, 0],
            Uprising=[1, 0, -1],
            Athyra=[1, 0, -1],
            Iorich=[0, 0, 1],
            Lyorn=[0, 1, -1],
            Yendi=[1, 0, -1],
            Oracle=[1, 0, -1],
            Issola=[1, -1, 0],
            Vallista=[1, -1, 0],
            Dragon=[0, -1, 1],
            Chreotha=[1, 0, -1],
            Tsalmoth=[1, -1, 0],
            Jhegaala=[1, -1, 0],
        ),
        Jhegaala=Questions(
            Enchantress=[0, 0, 1],
            Court=[-1, 1, 0],
            Duel=[0, 1, 0],
            Jhereg=[0, -1, 1],
            Phoenix=[0, 0, 1],
            Uprising=[-1, 1, 0],
            Athyra=[1, 0, 0],
            Iorich=[0, 0, 1],
            Lyorn=[-1, 0, 1],
            Yendi=[0, 1, 1],
            Oracle=[0, 1, 1],
            Issola=[0, 0, 1],
            Vallista=[0, 0, 1],
            Dragon=[-1, 1, 0],
            Chreotha=[0, 0, 1],
            Tsalmoth=[0, 0, 1],
            Jhegaala=[0, -1, 1],
        ),
        Chreotha=Questions(
            Enchantress=[-1, 0, 1],
            Court=[-1, 1, 1],
            Duel=[-1, 1, 1],
            Jhereg=[-1, 0, 1],
            Phoenix=[-1, 1, 1],
            Uprising=[-1, 1, 0],
            Athyra=[-1, 1, 1],
            Iorich=[1, 1, 0],
            Lyorn=[-1, 1, 1],
            Yendi=[-1, 1, 1],
            Oracle=[-1, 0, 1],
            Issola=[-1, 1, 1],
            Vallista=[0, -1, 1],
            Dragon=[1, -1, 1],
            Chreotha=[-1, 0, 1],
            Tsalmoth=[-1, 1, 1],
            Jhegaala=[0, 1, 1],
        ),
        Teckla=Questions(
            Enchantress=[-1, 0, 1],
            Court=[-1, 0, 1],
            Duel=[-1, 1, 1],
            Jhereg=[-1, 1, 0],
            Phoenix=[-1, 0, 1],
            Uprising=[-1, 1, 0],
            Athyra=[-1, 1, 0],
            Iorich=[1, 0, -1],
            Lyorn=[-1, 1, 1],
            Yendi=[-1, 0, 1],
            Oracle=[-1, 0, 1],
            Issola=[-1, 1, 0],
            Vallista=[-1, 0, 1],
            Dragon=[-1, 1, 1],
            Chreotha=[-1, 1, 0],
            Tsalmoth=[0, 1, 1],
            Jhegaala=[-1, 0, 1],
        ),
        Tsalmoth=Questions(
            Enchantress=[0, 1, 1],
            Court=[0, 0, 1],
            Duel=[-1, 1, 0],
            Jhereg=[-1, 1, 0],
            Phoenix=[1, 0, 0],
            Uprising=[0, 1, -1],
            Athyra=[-1, 1, 0],
            Iorich=[1, -1, 0],
            Lyorn=[1, 0, 0],
            Yendi=[1, 0, 0],
            Oracle=[-1, 0, 1],
            Issola=[1, 0, -1],
            Vallista=[0, 0, 1],
            Dragon=[-1, 0, 1],
            Chreotha=[1, 0, 0],
            Tsalmoth=[0, 1, 0],
            Jhegaala=[1, -1, 0],
        ),
        Vallista=Questions(
            Enchantress=[-1, 0, 1],
            Court=[-1, 0, 1],
            Duel=[-1, 0, 1],
            Jhereg=[-1, 1, 0],
            Phoenix=[0, 1, 0],
            Uprising=[-1, 1, 0],
            Athyra=[-1, 0, 1],
            Iorich=[1, 0, -1],
            Lyorn=[0, -1, 1],
            Yendi=[-1, 0, 1],
            Oracle=[-1, 0, 1],
            Issola=[0, 0, 1],
            Vallista=[0, -1, 1],
            Dragon=[-1, 0, 1],
            Chreotha=[-1, 0, 1],
            Tsalmoth=[-1, 1, 0],
            Jhegaala=[1, -1, 0],
        ),
        Iorich=Questions(
            Enchantress=[-1, 1, 1],
            Court=[-1, 0, 1],
            Duel=[-1, 1, 0],
            Jhereg=[-1, 1, 0],
            Phoenix=[0, 1, 0],
            Uprising=[-1, 1, 0],
            Athyra=[-1, 0, 1],
            Iorich=[1, -1, -1],
            Lyorn=[1, -1, 0],
            Yendi=[0, 0, 1],
            Oracle=[-1, 0, 1],
            Issola=[1, -1, 0],
            Vallista=[-1, 0, 1],
            Dragon=[-1, 1, 0],
            Chreotha=[-1, 0, 1],
            Tsalmoth=[-1, 1, 0],
            Jhegaala=[1, -1, 0],
        ),
        Hawk=Questions(
            Enchantress=[-1, 0, 1],
            Court=[-1, 0, 1],
            Duel=[-1, 0, 1],
            Jhereg=[-1, 1, 0],
            Phoenix=[0, 0, 1],
            Uprising=[-1, 1, 0],
            Athyra=[-1, 0, 1],
            Iorich=[1, 0, -1],
            Lyorn=[-1, 0, 1],
            Yendi=[-1, 0, 1],
            Oracle=[-1, 1, 0],
            Issola=[1, -1, 0],
            Vallista=[-1, -1, 1],
            Dragon=[-1, 0, 1],
            Chreotha=[-1, 0, 1],
            Tsalmoth=[-1, 1, 0],
            Jhegaala=[0, -1, 1],
        ),
    )