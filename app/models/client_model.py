from tortoise.models import Model
from tortoise import fields


class Client(Model):
    # id = Column(Integer, primary_key=True)
    id = fields.IntField(pk=True)
    
    # type_identity_id_fk = Column(Integer, ForeignKey('identities_type.id'))
    # type_identity = fields.ForeignKeyField(
    #     model_name='tiwala_backend.models.identity_types',
    #     related_name='clients'
    # )
    # type_identity = relationship('IdentityType', foreign_keys=[type_identity_id_fk]) #  SE BORRA
    
    # identification = Column(String(30), nullable=False)
    identification = fields.CharField(max_length=30)

    # names = Column(String(150), nullable=False)
    names = fields.CharField(max_length=150)
    # last_names = Column(String(150), nullable=False)
    last_names = fields.CharField(max_length=150)
    # full_names = Column(String(300), nullable=False)  # SE BORRA
    
    # country_id_fk = Column(Integer, ForeignKey('countries.id'))
    # country = relationship('Country', foreign_keys=[country_id_fk])
    # country = fields.ForeignKeyField(
    #     model_name='tiwala_backend.models.country',
    #     related_name='clients',
    # )

    # department_id_fk = Column(Integer, ForeignKey('departments.id'))
    # department = relationship('Department', foreign_keys=[department_id_fk])
    department = fields.ForeignKeyField(
        model_name='models.Department',
        related_name='clients',
    )

    # city_id_fk = Column(Integer, ForeignKey('cities.id'))
    # city = relationship('City', foreign_keys=[city_id_fk])
    city = fields.ForeignKeyField(
        model_name='models.City',
        related_name='clients',
    )
    
    # postal_code = Column(String(10), nullable=True)
    postal_code = fields.CharField(max_length=10, null=True)

    # client_contact = relationship('ClientContact', back_populates='client')
    # client_contact: fields.ReverseRelation['ClientContact']

    # referrals = relationship('Referred', back_populates='client')

    # referrals: fields.ReverseRelation['Referred']    
    
    # proposals = relationship('Proposal', back_populates='client')

    # proposals: fields.ReverseRelation['Proposal']

    # address = Column(String(200), nullable=False)
    address = fields.CharField(max_length=200)
    # phone_number = Column(String(30), nullable=False)
    phone_number = fields.CharField(max_length=150)
    # email_contact = Column(String(150), nullable=False)
    email_address = fields.CharField(max_length=150)
    # electronic_invoice = Column(String(150), nullable=True)
    electronic_invoice = fields.CharField(max_length=150, null=True)

    # ciiu_id_fk = Column(Integer, ForeignKey('ciiu_code.id'))
    # ciiu = relationship('CiiuCode', foreign_keys=[ciiu_id_fk])
    # ciiu = fields.ForeignKeyField(
    #     model_name='tiwala_backend.models.ciiu_code',
    #     related_name='clients',
    # )

    # occupation_id_fk = Column(Integer, ForeignKey('occupations.id'))
    # occupation = relationship('Occupation', foreign_keys=[occupation_id_fk])
    # occupation = fields.ForeignKeyField(
    #     model_name='tiwala_backend.models.occupation',
    #     related_name='clients',
    # )

    # income = Column(Float, nullable=False)
    income = fields.FloatField()
    # constitution_date = Column(DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    constitution_date = fields.DateField()
    # habeas_data = Column(Float, nullable=False)
    habeas_data = fields.BooleanField()
    # habeas_data_date = Column(DateTime, nullable=False, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    habeas_data_date = fields.DateField()

    # segment_id_fk = Column(Integer, ForeignKey('segments.id'))
    # segment = relationship('Segment', foreign_keys=[segment_id_fk], back_populates='client')
    # segment = fields.ForeignKeyField(
    #     model_name='tiwala_backend.models.segment',
    #     related_name='clients',
    # )
    
    # client_campuses = relationship('CampusClient', back_populates='client')
    # client_campuses: fields.ReverseRelation['CampusClient']

    # state_id_fk = Column(Integer, ForeignKey('states.id'))
    # state = relationship('State', foreign_keys=[state_id_fk], back_populates='clients')
    # state = fields.ForeignKeyField(
    #     model_name='tiwala_backend.models.state'
    # )
    
    def __repr__(self):
        return f'{self.id} | {self.names} | {self.last_names} | {self.identification}'