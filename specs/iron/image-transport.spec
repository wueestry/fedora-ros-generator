# Meta Package
Name:           ros-iron-image-transport
Version:        4.2.4
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/image_transport
Summary:        Meta package for ros2-iron-image_transport and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-image_transport
Requires:       ros2-iron-image_transport-devel

Obsoletes: ros-iron-image-transport < 4.2.4-1

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
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.4.2.4-1
- Update to latest release
