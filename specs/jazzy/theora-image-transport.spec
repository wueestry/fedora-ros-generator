# Meta Package
Name:           ros-jazzy-theora-image-transport
Version:        4.0.4
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/wiki/image_transport_plugins
Summary:        Meta package for ros2-jazzy-theora_image_transport and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-theora_image_transport
Requires:       ros2-jazzy-theora_image_transport-devel

Obsoletes: ros-jazzy-theora-image-transport < 4.0.4-1

%description
Theora_image_transport provides a plugin to image_transport for
transparently sending an image stream encoded with the Theora codec.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Mar 14 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.0.4-1
- Update to latest release
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.0.3-1
- Update to latest release
* Sat Aug 03 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.0.2-1
- Update to latest release
