# Meta Package
Name:           ros-jazzy-image-transport
Version:        5.1.3
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/image_transport
Summary:        Meta package for ros2-jazzy-image_transport and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-image_transport
Requires:       ros2-jazzy-image_transport-devel

Obsoletes: ros-jazzy-image-transport < 5.1.3-1

%description
image_transport should always be used to subscribe to and publish
images. It provides transparent support for transporting images in
low-bandwidth compressed formats. Examples (provided by separate
plugin packages) include JPEG/PNG compression and Theora streaming
video.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.5.1.3-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.5.1.2-1
- Update to latest release
