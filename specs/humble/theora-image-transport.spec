# Meta Package
Name:           ros-humble-theora-image-transport
Version:        2.5.2
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/wiki/image_transport_plugins
Summary:        Meta package for ros2-humble-theora_image_transport and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-theora_image_transport
Requires:       ros2-humble-theora_image_transport-devel

Obsoletes: ros-humble-theora-image-transport < 2.5.2-1

%description
Theora_image_transport provides a plugin to image_transport for
transparently sending an image stream encoded with the Theora codec.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 12 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.5.2-1
- Update to latest release
