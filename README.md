# 2D-DFT in image Processing

The Fourier Transform is an important image processing tool which is used to decompose an image into its sine and cosine components. The output of the transformation represents the image in the Fourier or frequency domain, while the input image is the spatial domain equivalent. In the Fourier domain image, each point represents a particular frequency contained in the spatial domain image.

The Fourier Transform is used in a wide range of applications, such as image analysis, image filtering, image reconstruction and image compression. 


## How it works
As we are only concerned with digital images, we will restrict this discussion to the Discrete Fourier Transform (DFT).

The DFT is the sampled Fourier Transform and therefore does not contain all frequencies forming an image, but only a set of samples which is large enough to fully describe the spatial domain image. The number of frequencies corresponds to the number of pixels in the spatial domain image, i.e. the image in the spatial and Fourier domain are of the same size.

For a square image of size N×N, the two-dimensional DFT is given by:

<img src="https://render.githubusercontent.com/render/math?math=X_{lm} =   \sum_{j=0}^{N-1}\sum_{k=0}^{M-1}X_{jk} e^{-2\pi i (\frac{jl}{N}%2B\frac{km}{M})}">



where f(a,b) is the image in the spatial domain and the exponential term is the basis function corresponding to each point F(k,l) in the Fourier space. The equation can be interpreted as: the value of each point F(k,l) is obtained by multiplying the spatial image with the corresponding base function and summing the result.

The basis functions are sine and cosine waves with increasing frequencies, i.e. F(0,0) represents the DC-component of the image which corresponds to the average brightness and F(N-1,N-1) represents the highest frequency.

In a similar way, the Fourier image can be re-transformed to the spatial domain. The inverse Fourier transform is given by:

<img src="https://render.githubusercontent.com/render/math?math=X_{lm} = \frac{1}{N} \frac{1}{M}  \sum_{j=0}^{N-1}\sum_{k=0}^{M-1}X_{jk} e^{ 2\pi i (\frac{jl}{N}%2B\frac{km}{M})}">



The Fourier Transform produces a complex number valued output image which can be displayed with two images, either with the real and imaginary part or with magnitude and phase. In image processing, often only the magnitude of the Fourier Transform is displayed, as it contains most of the information of the geometric structure of the spatial domain image. However, if we want to re-transform the Fourier image into the correct spatial domain after some processing in the frequency domain, we must make sure to preserve both magnitude and phase of the Fourier image.

The Fourier domain image has a much greater range than the image in the spatial domain. Hence, to be sufficiently accurate, its values are usually calculated and stored in float values. 

## Apply Low-Pass or High-pass filter in Fourie Domain
Frequency filters process an image in the frequency domain. The image is Fourier transformed, multiplied with the filter function and then re-transformed into the spatial domain. Attenuating high frequencies results in a smoother image in the spatial domain, attenuating low frequencies enhances the edges.

All frequency filters can also be implemented in the spatial domain and, if there exists a simple kernel for the desired filter effect, it is computationally less expensive to perform the filtering in the spatial domain. Frequency filtering is more appropriate if no straightforward kernel can be found in the spatial domain, and may also be more efficient.

## How It Works

Frequency filtering is based on the Fourier Transform. (For the following discussion we assume some knowledge about the Fourier Transform, therefore it is advantageous if you have already read the corresponding worksheet.) The operator usually takes an image and a filter function in the Fourier domain. This image is then multiplied with the filter function in a pixel-by-pixel fashion:

<img src="https://render.githubusercontent.com/render/math?math=G(k,l) =H(k,l)*F(k,l)">
    

where F(k,l) is the input image in the Fourier domain, H(k,l) the filter function and G(k,l) is the filtered image. To obtain the resulting image in the spatial domain, G(k,l) has to be re-transformed using the inverse Fourier Transform.

Since the multiplication in the Fourier space is identical to convolution in the spatial domain, all frequency filters can in theory be implemented as a spatial filter. However, in practice, the Fourier domain filter function can only be approximated by the filtering kernel in spatial domain.

The form of the filter function determines the effects of the operator. There are basically three different kinds of filters: lowpass, highpass and bandpass filters. A low-pass filter attenuates high frequencies and retains low frequencies unchanged. The result in the spatial domain is equivalent to that of a smoothing filter; as the blocked high frequencies correspond to sharp intensity changes, i.e. to the fine-scale details and noise in the spatial domain image.
A highpass filter, on the other hand, yields edge enhancement or edge detection in the spatial domain, because edges contain many high frequencies. Areas of rather constant graylevel consist of mainly low frequencies and are therefore suppressed.
A bandpass attenuates very low and very high frequencies, but retains a middle range band of frequencies. Bandpass filtering can be used to enhance edges (suppressing low frequencies) while reducing the noise at the same time (attenuating high frequencies).

The most simple lowpass filter is the ideal lowpass. It suppresses all frequencies higher than the cut-off frequency Eqn:eqnfreq3 and leaves smaller frequencies unchanged:

<img src="https://render.githubusercontent.com/render/math?math=H(u,v) = 1-> when D(u,v) ≤ D0 , otherwise = 0">


In most implementations, <img src="https://render.githubusercontent.com/render/math?math=D0"> is given as a fraction of the highest frequency represented in the Fourier domain image.
