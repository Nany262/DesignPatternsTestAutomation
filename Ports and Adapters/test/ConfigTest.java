package co.com.bancolombia.ehauth.config;

import co.com.bancolombia.ehauth.MainApplication;
import co.com.bancolombia.ehauth.usecase.AuthCodeTokenUsecase;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.reactivecommons.utils.ObjectMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

import static org.junit.Assert.assertNotNull;

@RunWith(SpringJUnit4ClassRunner.class)
@SpringBootTest(classes = MainApplication.class)
public class BeanConfigTest {

    @Autowired
    private ObjectMapper objectMapper;
    @Autowired
    private AuthCodeTokenUsecase authCodeTokenUsecase;

    @Test
    public void objectMapper() {
        assertNotNull(objectMapper);
    }

    @Test
    public void authCodeTokenUsecase() {
        assertNotNull(authCodeTokenUsecase);
    }
}