# Meta Package
Name:           ros-humble-image-transport
Version:        3.1.9
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/image_transport
Summary:        Meta package for ros2-humble-image_transport and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-image_transport
Requires:       ros2-humble-image_transport-devel

Obsoletes: ros-humble-image-transport < 3.1.9-1

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
* Wed Mar 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.1.9-1
- update to latest release
* Mon Feb 19 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.1.8-1
- Update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.1.7-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.1.7-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.1.7-1
- update to latest upstream release
* Tue Aug 08 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.1.6-1
- update to latest upstream
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.1.5-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.1.12.0-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.1.5-1
- Initial humble build
